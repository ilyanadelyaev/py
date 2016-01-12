class Meta(type):
    def __iter__(self):
        for i in self._items:
            yield i


class RegIter(object):
    __metaclass__ = Meta

    _items = []

    def __new__(cls, *args, **kw):
        obj = super(RegIter, cls).__new__(cls, *args, **kw)
        cls._items.append(obj)
        return obj

    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return self.__class__.__name__ + '.' + self.val


x = RegIter('x')
y = RegIter('y')
z = RegIter('z')

for i in RegIter:
    print i
