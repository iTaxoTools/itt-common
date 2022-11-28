
"""Utility classes and functions"""


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

    def __iter__(self):
        return iter(self.values())


def override(f):
    return f
