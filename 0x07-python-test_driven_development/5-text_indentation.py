#!/usr/bin/python3
"""The text_indentation function"""


def text_indentation(text):
    """Function that set sentences with a new line

    Args:
        text (str): text to be formated
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    else:
        idx = 0
        for char in text:
            if idx == 0:
                if char == " ":
                    continue
                else:
                    idx = 1
            if idx == 1:
                if "." in char or "?" in char or ":" in char:
                    print(char + '\n')
                    idx = 0
                else:
                    print(char, end="")
