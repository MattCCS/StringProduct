"""
Brute-forces the solution for the String-Product Problem.

Tactics:
- check whether length would even be longer first (O(c) vs O(n))
- memoize all lettersets on load
- discard shorter words with equivalent lettersets
"""

import itertools
import time
import sys


def filter_by_lettersets(words):
    """
    Convert the wordlist into a mapping of {letterset -> (length, word)}.
    Remove equivalent or lesser-value words with the same letterset.
    """
    lettersets = {}

    for word in words:
        letterset = frozenset(word)
        length = len(word)
        if letterset not in lettersets or length > lettersets[letterset][0]:
            lettersets[letterset] = (length, word)

    return lettersets


def solve(filename):
    with open(filename) as infile:
        words = infile.read().splitlines()

    lettersets = filter_by_lettersets(words)

    best_score = -1
    best_words = None

    word_pairs = itertools.combinations(lettersets.items(), 2)
    for (val1, val2) in word_pairs:
        (set1, (len1, word1)) = val1
        (set2, (len2, word2)) = val2

        new_score = len1 * len2
        if new_score > best_score:
            if not (set1 & set2):
                best_score = new_score
                best_words = (word1, word2)
                print(best_words)

    return (best_score, best_words)


def main():
    t0 = time.time()
    print(solve(sys.argv[1]))
    t1 = time.time()
    print(f"Time taken: {t1 - t0} seconds")


if __name__ == '__main__':
    main()
