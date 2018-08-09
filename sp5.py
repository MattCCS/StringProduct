"""
Brute-forces the solution for the String-Product Problem.

Tactics:
- memoize all lettersets on load
- discard shorter words with equivalent lettersets
- deal with word indices rather than strings (never copy strings)
- iterate over word pairs in order of max product
    - bin words by length
- check whether length would even be longer first (O(c) vs O(n))
"""

import collections
import itertools
import sys
import time


def mask(bytearr):
    """Returns a mask of 122 bits"""
    word_mask = 0
    for c in bytearr:
        word_mask |= 1 << c
    return word_mask


def filter_by_lettersets(words):
    """
    Convert the wordlist into a mapping of {letterset -> (length, word)}.
    Remove equivalent or lesser-value words with the same letterset.
    """
    lettersets = {}

    for (i, word) in enumerate(words):
        letterset = mask(word)
        length = len(word)
        if letterset not in lettersets or length > lettersets[letterset][0]:
            lettersets[letterset] = (length, word)

    return lettersets


def generate_length_bins(length_word_pairs):
    length_bins = collections.defaultdict(lambda: collections.defaultdict(str))

    for (letterset, (length, word)) in length_word_pairs:
        length_bins[length][letterset] = word

    return length_bins


def generate_max_product_pairs(word_lengths):
    """
    Returns every pair of word lengths sorted by maximum product
    (largest first).
    """
    word_length_pairs = itertools.product(word_lengths, repeat=2)
    return sorted(word_length_pairs, key=lambda p: p[0] * p[1], reverse=True)


def solve(filename):
    with open(filename, "rb") as infile:
        words = infile.read().splitlines()

    lettersets = filter_by_lettersets(words)
    length_bins = generate_length_bins(lettersets.items())
    word_lengths = frozenset(length_bins.keys())
    max_product_pairs = generate_max_product_pairs(word_lengths)

    for (len1, len2) in max_product_pairs:
        lettersets1 = length_bins[len1].keys()

        if len1 == len2:
            letterset_pairs = itertools.combinations(lettersets1, 2)
        else:
            lettersets2 = length_bins[len2].keys()
            letterset_pairs = itertools.product(lettersets1, lettersets2)

        for (set1, set2) in letterset_pairs:
            if not (set1 & set2):
                # word_index1 = length_bins[len1][set1]
                # word_index2 = length_bins[len2][set2]
                # word1 = words[word_index1]
                # word2 = words[word_index2]

                word1 = length_bins[len1][set1]
                word2 = length_bins[len2][set2]

                best_score = len1 * len2
                best_words = (word1, word2)
                print(best_words)
                return (best_score, best_words)

    raise RuntimeError("No valid pair found!")


def main():
    t0 = time.time()
    print(solve(sys.argv[1]))
    t1 = time.time()
    print(f"Time taken: {t1 - t0} seconds")


if __name__ == '__main__':
    main()
