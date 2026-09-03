#!/usr/bin/env python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements between two sets.

    Args:
        set_1 (set): The first input set.
        set_2 (set): The second input set.

    Returns:
        set: A new set containing the common elements
        between the two input sets.
    """
    return set_1 & (set_2)
