# ameliore watson4 en ajoutant a 'while True' pour faire une boucle infinie
# bien penser à ajouter une condition de sortie avec des exit_words

def init_watson(config_file_name):
    """
    load the config_file_name and returns set of 
    sentiment words in a tuple
    
    parameter
    ---------
    config_file_name: the name of the file to load
    
    return
    ------
    the tuple of sets (positive_words, negative_words, exit_words)
    """
    with open(config_file_name, "r", encoding="utf8") as f:
        for line in f:
            # we remove the \n char is if it is at the end of the line
            # it might not be the case at the end of the file
            if line[-1] == "\n":
                line = line[:-1]
            if line:
                line = line.split()
                start = line[0]
                if start == "POSITIVE":
                    positive_words = set(line[1:])
                elif start == "NEGATIVE":
                    negative_words = set(line[1:])
                elif start == "EXIT":
                    exit_words = set(line[1:])

    return positive_words, negative_words, exit_words


def test_phrase_sentiment(phrase, sentiment):
    """
    take a sentence and return True if any words
    in sentiment is in phrase
    
    parameter
    ---------
    phrase: a set of str
    sentiment: a set of str containing sentiment words
    
    return
    ------
    the interection between the words in the sentence and the words
    in the sentiment set
    """
    return phrase.intersection(sentiment)


def start():
    """
    demarre le docteur watson

    parametre
    ---------
    aucun

    return
    ------
    None
    """
    positive_words, negative_words, exit_words = init_watson(
        "watson-config.txt"
    )
    
    message = 'bonjour, à vous: '
    while True:
        phrase = set(input(message).lower().split())

        if test_phrase_sentiment(phrase, negative_words):
            message = "Ohhhh, c'est triste, mais encore...\n"
        elif test_phrase_sentiment(phrase, positive_words):
            message = "C'est super, mais encore...\n"
        elif test_phrase_sentiment(phrase, exit_words):
            break
        elif not phrase:
            message = "Tu n'es pas bavard. Que peux-tu me dire...\n"
        else:
            message = "je ne comprends pas...\n"

    print("C'est fini, au revoir !")


start()