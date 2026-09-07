#!/usr/bin/env python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The result of the division, or None if division fails.
    """
    res = None
    try:
        res = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(res))
    return res
