#!/usr/bin/python3
"""MyInt Class"""


class MyInt(int):
    """MyInt Class"""

    def __eq__(self, other):
        """Equality method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Not wqual method"""
        return super().__eq__(other)
