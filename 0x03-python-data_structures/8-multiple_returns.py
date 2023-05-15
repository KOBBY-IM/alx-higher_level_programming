#!/usr/bin/python3

def multiple_returns(sentence):
    # Check for empty string.
    if not sentence:
        return (0, None)

    # Get the length of the string.
    length = len(sentence)

    # Get the first character of the string.
    first_character = sentence[0]

    return (length, first_character)
