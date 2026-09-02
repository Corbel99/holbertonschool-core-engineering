#!/usr/bin/env python3

def replace_in_list(my_list, idx, element):
    """Replaces an element in a list like in C.

    Args:
    my_list (list): The list to replace the element in.
    idx (int): The index of the element to replace.
    element: The new element to place at the specified index.
    Returns:
    The list with the element replaced if the index is valid
    otherwise the original list."""

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
