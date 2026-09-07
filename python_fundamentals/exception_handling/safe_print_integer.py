#!/usr/bin/env python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        True if value is an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
