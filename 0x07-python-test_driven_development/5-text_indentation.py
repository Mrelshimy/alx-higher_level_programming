#!/usr/bin/python3
"""module for text indentation by delimeter"""


def text_indentation(text):
    """ Function to indent text based on ? , :

        Args:
            text: input string

        Raises:
            TypeError: Raise if text is not string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for dmtr in ":.?":
        text = (dmtr + "\n\n").join(
              [index.strip(" ") for index in text.split(dmtr)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
