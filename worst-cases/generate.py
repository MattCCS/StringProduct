"""
Generates the worst-case scenario wordlist for a given max word length.

Be careful with inputs above 5!
"""

import itertools
import string
import sys


LETTERS = string.ascii_lowercase.encode("utf-8")


def main():
    length = int(sys.argv[1])

    with open(f"{length}.txt", "wb") as outfile:
        for i in range(1, length + 1):
            iterator = (bytearray(chars) for chars in itertools.product(LETTERS, repeat=i))
            for word in iterator:
                outfile.write(word + b"\n")


if __name__ == '__main__':
    main()
