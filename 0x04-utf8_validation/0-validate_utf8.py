#!/usr/bin/python3
"""
Module for a method that determines if
a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    num_bytes = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
