import os

class Content:
    # base level class for the content
    def __init__(self, path):
        self._path = os.path.expanduser(path)

    @property
    def path(self):
        return self._path
