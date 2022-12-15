"""
toying around the MOTUS game
"""

from pathlib import Path
from itertools import islice
from functools import reduce
from enum import Enum, auto

from colorama import Back, Style

# on Enums: see https://docs.python.org/3/howto/enum.html
class Color(Enum):
    """
    the codes for creating an answer
    """

    RED = auto()     # full match
    YELLOW = auto()  # exists in another location
    WHITE = auto()   # not in word at all

    def outline(self, message: str):
        """
        a string colored with that color
        """
        if self.name == "RED":
            beg, end = Back.RED, Style.RESET_ALL
        elif self.name == "YELLOW":
            beg, end = Back.YELLOW, Style.RESET_ALL
        else:
            beg, end = Back.WHITE, Style.RESET_ALL
        return f"{beg} {message} {end} "
    def __eq__(self, other):
        # surprisingly this is required...
        return self.name == other.name

# shortcuts
R, Y, W = Color.RED, Color.YELLOW, Color.WHITE


class Answer:
    """
    primarily an ordered tuple of colors
    """
    def __init__(self, *colors: Color):
        # no need to transform into tuple
        self.colors = colors

    def __eq__(self, other):
        return self.colors == other.colors

    def __iter__(self):
        return iter(self.colors)

    def red(self):
        """
        is it a right answer ?
        """
        return all(x == Color.RED for x in self.colors)


class Attempt:
    """
    record the fact that you get an answer for a word
    """
    def __init__(self, word: str, answer: Answer):
        self.word = word
        self.answer = answer

    def __repr__(self):
        return "".join(color.outline(f" {char} ")
                       for char, color in zip(self.word, self.answer))

    def __iter__(self):
        """
        allow to unpack e.g.
        word, answer = attempt
        """
        yield self.word
        yield self.answer

    def __len__(self):
        return len(self.word)

    def __eq__(self, other):
        return self.answer == other.answer

    def absent_chars(self):
        """
        returns a set of chars that are only marked WHITE
        so we know they are not in the hidden word
        """
        # but of course we must be a little careful
        definitely_there = {
            char for char, color in zip(self.word, self.answer)
            if color != Color.WHITE
        }
        apparently_not_there = {
            char for char, color in zip(self.word, self.answer)
            if color == Color.WHITE
        }
        return apparently_not_there - definitely_there


# define this alias for type hinting
Attempts = list[Attempt]


class Hidden:

    """
    the algorithm to compute an Answer
    actually we return an Attempt as it it way nicer to look at
    """
    def __init__(self, word: str):
        self.word = word

    def __len__(self):
        return len(self.word)

    def attempt(self, typed: str) -> Attempt:
        """
        returns the 'attempt': when a user types the typed word,

        there is a subtlety with chars appearing several times,
        so a few examples:

        | hidden | typed | result | comment |
        | ABC    | AAA   | RWW    | a single match |
        | ABCA   | AAAA  | RWWR   | two matches    |
        | ABCA   | AAAY  | RWYW   | one exact match and one partial |
        """
        if len(self) != len(typed):
            raise ValueError(f"length mismatch {len(self)} != {len(typed)}")
        # first pass is to spot exact matches
        red_indices = {
            index for index, (ct, ch) in enumerate(zip(typed, self.word))
            if ct == ch}
        # the remaining chars in the hidden word
        remaining = [char for index, char in enumerate(self.word)
                     if index not in red_indices]
        # now let's focus on the other characters
        yellow_indices = set()
        for index, c in enumerate(typed):
            if index in red_indices:
                continue
            # do we have this char in the remaining chars ?
            # if yes, remove it
            try:
                remaining.remove(c)
                yellow_indices.add(index)
            # if not, it's OK, we'll fill this index with WHITE later
            except ValueError:
                pass
        # fill the result
        result = []
        for i in range(len(self)):
            if i in red_indices:
                result.append(Color.RED)
            elif i in yellow_indices:
                result.append(Color.YELLOW)
            else:
                result.append(Color.WHITE)
        return Attempt(typed, Answer(*result))


class Dictionary:

    """
    primarily a set of words
    """

    def __init__(self, filename):
        self.filename = filename
        with Path(self.filename).open(encoding="utf-8") as feed:
            self.words = {line.strip().lower() for line in feed}

    def __contains__(self, word: str):
        return word.lower() in self.words

    def __iter__(self):
        return iter(self.words)

    def all_words_of_length(self, length: int):
        """
        iterator on all words of that length
        """
        for word in self:
            if len(word) == length:
                yield word

    def sample_of_length(self, length) -> str:
        """
        for convenience, returns one word of length length
        """
        # we have already the logic to extract all words, so just take
        # the first one using islice, because all_words_of_length())
        # returns an iterator, so we cannot use regular [] here
        # also, nicely handle the case where length is too large
        # and there is not word of that length
        try:
            return next(islice(self.all_words_of_length(length), None, 1))
        except StopIteration:
            pass

    def compatible_words(self, attempts: Attempts) -> set[str]:
        """
        given what has been tried so far (the attempts)
        returns the words that could fit
        """
        # we assume all attempts have the same length
        length = len(attempts[0])
        # first we rule out all words that have any of the
        # chars that we know for sure are not present
        # this is a union of sets
        absent_chars = reduce(
            lambda s1, s2: s1 | s2,
            (attempt.absent_chars() for attempt in attempts)
        )
        for attempt in attempts:
            print(f"{attempt=} -> {attempt.absent_chars()=}")
        print(f"union of all -> {absent_chars}")
        # we keep only words that have no intersection with
        # absent_chars
        comb = {
            word for word in self.all_words_of_length(length)
            if not (set(word) & set(absent_chars))}
        print(f"{len(comb)=}")
        print(f"{'francais' in comb=}")
        def match(candidate):
            # does a candidate word yield the same answers
            # than the ones provided in parameter ?
            return all(
                Hidden(candidate).attempt(attempt.word) == attempt
                for attempt in attempts)

        return { word for word in comb if match(word) }
