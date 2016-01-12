class Deque(object):
    class _Node(object):
        def __init__(self, prev_node, next_node, data):
            self._next_node = next_node
            self._prev_node = prev_node
            self.data = data

        def __str__(self):
            return self.data

        def __repr__(self):
            return '< {} {} {} >'.format(
                '<-' if self._prev_node else '|-',
                self.data,
                '->' if self._next_node else '-|',
            )

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
        self._last_node = None
        self.extend(it)

    def __iter__(self):
        return Deque._Iter(self)

    def __len__(self):
        return self.length

    def __contains__(self, v):
        for d in self:
            if d == v:
                return True
        return False

    def push(self, v):
        node = Deque._Node(self._last_node, None, v)
        if self._first_node is None:
            self._first_node = node
        if self._last_node:
            self._last_node._next_node = node
        self._last_node = node
        self.length += 1

    def push_left(self, v):
        node = Deque._Node(None, self._first_node, v)
        if self._last_node is None:
            self._last_node = node
        if self._first_node:
            self._first_node._prev_node = node
        self._first_node = node
        self.length += 1

    def pop(self):
        if self._last_node is None:
            raise IndexError('pop from empty list')
        if self._last_node._prev_node:
            self._last_node._prev_node._next_node = self._last_node._next_node
        else:
            self._first_node = None
        data = self._last_node.data
        self._last_node = self._last_node._prev_node
        self.length -= 1
        return data

    def pop_left(self):
        if self._first_node is None:
            raise IndexError('pop from empty list')
        if self._first_node._next_node:
            self._first_node._next_node._prev_node = self._first_node._prev_node
        else:
            self._last_node = None
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
    dq = Deque()

    dq.push_left(1)
    dq.push_left(2)
    dq.push_left(3)
    dq.push_left(4)

    assert len(dq) == 4
    assert 10 not in dq
    assert 1 in dq

    dq.push(10)
    dq.push(20)
    dq.push(30)
    dq.push(40)

    assert len(dq) == 8
    assert 10 in dq
    assert 1 in dq

    assert dq.pop_left() == 4
    assert dq.pop_left() == 3
    assert dq.pop_left() == 2
    assert dq.pop_left() == 1
    assert dq.pop_left() == 10
    assert dq.pop_left() == 20
    assert dq.pop_left() == 30
    assert dq.pop_left() == 40
    try:
        dq.pop_left()
        assert False
    except IndexError:
        assert True

    assert len(dq) == 0

    dq.push_left(1)
    dq.push(10)

    assert len(dq) == 2
    assert 10 in dq
    assert 1 in dq

    assert dq.pop() == 10
    assert dq.pop() == 1
    try:
        dq.pop()
        assert False
    except IndexError:
        assert True
    assert len(dq) == 0
