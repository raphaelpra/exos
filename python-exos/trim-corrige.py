#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser

LINE_STARTERS = [
    "# solution",
    "## solution",
    "# # solution",
    "# ## solution",
]

def trim_solution(in_filename, out_filename):
    found = False
    with (open(in_filename) as reader, open(out_filename, 'w') as writer):
        for line in reader:
            if any(line.startswith(x) for x in LINE_STARTERS):
                break
            writer.write(line)

def output_filename(in_filename):
    result = in_filename.replace("-corrige", "")
    if result == in_filename:
        return None
    return result


def main():
    parser = ArgumentParser()
    parser.add_argument("corriges", nargs="+")
    parser.add_argument("-v", "--verbose", default=False, action='store_true')

    cli_args = parser.parse_args()
    corriges = cli_args.corriges

    def verbose(*args, **kwds):
        if cli_args.verbose:
            print(*args, **kwds)

    for corrige in corriges:
        student = output_filename(corrige)
        if not student:
            verbose(f"ignoring {corrige} - does not contain -corrige")
            continue

        p1, p2 = Path(corrige), Path(student)
        if not p1.exists():
            print("OOPS - input {p1} not found")
            continue
        if p2.exists() and p2.stat().st_mtime > p1.stat().st_mtime:
            verbose(f"ignoring {p1}, as {p2} is more recent")
            continue
        message = "created" if not p2.exists() else "overwritten"
        trim_solution(corrige, student)
        print(f"{student} {message}")

main()