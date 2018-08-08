"""
Generate a random subset of the given wordlist.
"""

import random
import sys


def main():
    infile_name = sys.argv[1]
    num = int(sys.argv[2])

    with open(infile_name) as infile:
        words = infile.read().splitlines()

    words = sorted(random.sample(words, num))
    sys.stdout.write("\n".join(words))


if __name__ == '__main__':
    main()
