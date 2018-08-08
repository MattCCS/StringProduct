"""
Brute-forces the solution for the String-Product Problem.

Tactics:
- check whether length would even be longer first (O(c) vs O(n))
"""

import itertools
import time
import sys


def is_valid_pair(word1, word2):
    """Return True if the words have no letters in common."""
    return not (set(word1) & set(word2))


def solve_bruteforce(filename):
    with open(filename) as infile:
        words = infile.read().splitlines()

    best_score = -1
    best_words = None

    word_pairs = itertools.combinations(words, 2)
    for (word1, word2) in word_pairs:
        new_score = len(word1) * len(word2)
        if new_score > best_score:
            if is_valid_pair(word1, word2):
                best_score = new_score
                best_words = (word1, word2)
                print(best_words)

    return (best_score, best_words)


def main():
    t0 = time.time()
    print(solve_bruteforce(sys.argv[1]))
    t1 = time.time()
    print(f"Time taken: {t1 - t0} seconds")


if __name__ == '__main__':
    main()
