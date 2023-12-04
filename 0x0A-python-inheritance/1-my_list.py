#!.usr/bin/python3
"""MyList Class"""


class MyList(list):
    """List class"""

    def print_sorted(self):
        """return a sorted list"""

        a = self[:]
        print(sorted(a))
