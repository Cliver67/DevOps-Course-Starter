class ViewModel:
    def __init__(self, items, todo, doing, done):
        self._items = items
        self._todo = todo
        self._doing = doing
        self._done = done
        

    @property
    def items(self):
        return self._items

    @property
    def todo(self):
        return self._todo

    @property
    def doing(self):
        return self._doing

    @property
    def done(self):
        return self._done
        