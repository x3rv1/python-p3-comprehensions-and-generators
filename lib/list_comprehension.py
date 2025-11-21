#!/usr/bin/env python3


def return_evens(sequence):
    """
    Returns a list of all even elements from a sequence of integers.
    """
    return [num for num in sequence if num % 2 == 0]

def make_exclamation(sentences):
    """
    Returns a list of sentences with exclamation marks added at the end.
    """
    return [sentence + "!" for sentence in sentences]
