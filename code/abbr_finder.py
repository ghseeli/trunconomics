""" These functions take in a list of words (from a corpus), and tries to identify abbreviations by looking at which words appear close to each other.
"""
import copy

import Levenshtein as lev

def weed_out_synonyms(word, potential_synonyms):
    """ Takes in a word and a list of 'supposed' synonyms, and deletes the ones whose Levenshtein distance is too high. """
    real_synonyms = set()
    for synonym in potential_synonyms:
        max_distance = abs(len(word) - len(synonym))
        abbr_len = min(len(word), len(synonym))
        forgiveness = round(1/7 * abbr_len)
        if lev.distance(word, synonym) <= max_distance + forgiveness:
            # Then it's a synonym!
            real_synonyms.add(synonym)
    return real_synonyms

def remove_too_long_words(word, potential_truncations):
    return [trunc for trunc in potential_truncations if len(trunc) < len(word)]
