"""
Brute-forces the solution for the String-Product Problem.

Tactics:
...
"""

import collections
import itertools
import sys
import time


class LazyWordset:
    """Right idea, but this has TOCTOU/concurrency bugs..."""

    def __init__(self, words):
        self.length = len(words)
        self.visited = {}
        self.unvisited = words

    def lazyitems(self):
        for (set, word) in self.visited.items():
            yield (set, word)

        while self.unvisited:
            word = self.unvisited.pop()
            set = mask(word)
            if set not in self.visited:
                self.visited[set] = word
                yield (set, word)


def mask(bytearr):
    """Returns a mask of 122 bits"""
    word_mask = 0
    for c in bytearr:
        word_mask |= 1 << c
    return word_mask


def group_words_by_length(words):
    words_by_length = collections.defaultdict(list)

    for word in words:
        words_by_length[len(word)].append(word)

    return words_by_length


def generate_max_product_pairs(word_lengths):
    """
    Returns every pair of word lengths sorted by maximum product
    (largest first).
    """
    word_length_pairs = itertools.product(word_lengths, repeat=2)
    return sorted(word_length_pairs, key=lambda p: p[0] * p[1], reverse=True)


def generate_wordset_pairs(words_by_length, max_product_pairs):
    """
    Yield wordset pairs in order of maximum product.
    """
    wordsets_by_length = {}

    def ensure(length):
        nonlocal wordsets_by_length
        nonlocal words_by_length
        if length not in wordsets_by_length:
            wordsets_by_length[length] = LazyWordset(words_by_length[length])
        return wordsets_by_length[length]

    for (length_1, length_2) in max_product_pairs:
        score = length_1 * length_2
        wordset_1 = ensure(length_1)
        wordset_2 = ensure(length_2)
        yield (score, (length_1, wordset_1), (length_2, wordset_2))


def solve(filename):
    with open(filename, "rb") as infile:
        words = infile.read().splitlines()

    words_by_length = group_words_by_length(words)

    word_lengths = frozenset(words_by_length.keys())
    max_product_pairs = generate_max_product_pairs(word_lengths)

    wordset_pairs = generate_wordset_pairs(words_by_length, max_product_pairs)

    for (score, (len1, wordset_1), (len2, wordset_2)) in wordset_pairs:

        # if len1 == len2:
        #     letterset_pairs = itertools.combinations(wordset_1.lazyitems(), 2)
        # else:
        #     letterset_pairs = itertools.product(wordset_1.lazyitems(), wordset_2.lazyitems())

        for (set1, word1) in wordset_1.lazyitems():
            for (set2, word2) in wordset_2.lazyitems():
                if not (set1 & set2):
                    best_score = score
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
