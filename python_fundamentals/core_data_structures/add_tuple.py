#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples element-wise.

Args:
    tuple_a (tuple): The first tuple.
    tuple_b (tuple): The second tuple.

Returns:
    A new tuple containing the sums of the first two elements.
    Missing elements are treated as 0.
"""
    if len(tuple_a) > 0:
        a0 = tuple_a[0]
    else:
        a0 = 0

    if len(tuple_a) > 1:
        a1 = tuple_a[1]
    else:
        a1 = 0

    if len(tuple_b) > 0:
        b0 = tuple_b[0]
    else:
        b0 = 0
    if len(tuple_b) > 1:
        b1 = tuple_b[1]
    else:
        b1 = 0

    return (a0 + b0, a1 + b1)
