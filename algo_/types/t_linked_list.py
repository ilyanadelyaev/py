class LinkedList(object):
    class _Node(object):
        def __init__(self, next_node, data):
            self._next_node = next_node
            self.data = data

        def __str__(self):
            return self.data

        def __repr__(self):
            return '< {} : {} >'.format(self.data, '->' if self._next_node else '-|')

    class _Iter(object):
        def __init__(self, obj):
            self.it = obj._first_node

        def next(self):
            if self.it is None:
                raise StopIteration
            else:
                data = self.it.data
                self.it = self.it._next_node
                return data

    def __init__(self, it=None):
        self.length = 0
        self._first_node = None
        self.extend(it)

    def __iter__(self):
        return LinkedList._Iter(self)

    def __len__(self):
        return self.length

    def __contains__(self, v):
        for d in self:
            if d == v:
                return True
        return False

    def push(self, v):
        self._first_node = LinkedList._Node(self._first_node, v)
        self.length += 1

    def pop(self):
        if self._first_node is None:
            raise IndexError('pop from empty list')
        data = self._first_node.data
        self._first_node = self._first_node._next_node
        self.length -= 1
        return data

    def extend(self, it):
        try:
            for v in it:
                self.push(v)
        except TypeError:
            pass


if __name__ == '__main__':
    s = LinkedList()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    assert len(s) == 4
    assert 4 in s
    assert 1 in s

    assert 4 == s.pop()
    assert 3 == s.pop()

    assert len(s) == 2
    assert 4 not in s
    assert 1 in s

    s.pop()
    s.pop()

    assert len(s) == 0
    assert 4 not in s
    assert 1 not in s

    s = LinkedList([10, 20])
    assert len(s) == 2
    assert 10 in s
    assert 20 in s
    assert s.pop() == 20
    assert s.pop() == 10
    assert len(s) == 0
