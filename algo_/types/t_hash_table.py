class HashTable(object):
    class _Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self._next = None

        def __repr__(self):
            return '( {} : {} {} )'.format(self.key, self.value, '->' if self._next else '-|')

    def __init__(self):
        self.length = 0
        self.table_size = 2 ** 8  #TODO: add dynamic here
        self.table = list(None for _ in xrange(self.table_size))

    def __str__(self):
        return str(self.__items())

    def __repr__(self):
        return self.__str__()

    def __cell(self, key):
        return hash(key) % self.table_size

    def __get(self, key):
        t = self.table[self.__cell(key)]
        while t:
            if t.key == key:
                return t
            t = t._next
        raise KeyError

    def __items(self):
        ret = []
        for t in self.table:
            while t:
                ret.append((t.key, t.value))
                t = t._next
        return ret

    def __len__(self):
        return self.length

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def get(self, key):
        return self.__get(key).value

    def add(self, key, value):
        # in table
        try:
            t = self.__get(key)
            t.value = value
            return
        except KeyError:
            pass
        # not in table
        c = self.__cell(key)
        if self.table[c] is None:
            self.table[c] = self._Node(key, value)
            self.length += 1
            return
        t = self.table[c]
        while t._next:
            t = t._next
        t._next = self._Node(key, value)
        self.length += 1

    def remove(self, key):
        c = self.__cell(key)
        if self.table[c] is None:
            raise KeyError
        prev = None
        cur = self.table[c]
        while cur:
            if cur.key == key:
                if prev is None:
                    self.table[c] = cur._next
                else:
                    prev._next = cur._next
                self.length -= 1
                return
            prev = cur
            cur = cur._next
        raise KeyError


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    I = [(i, i*10) for i in I]

    h = HashTable()

    for k, v in I:
        h.add(k, v)

    assert len(h) == len(I)

    for k, v in I:
        assert k in h
        assert h.get(k) == v

    try:
        h.remove(-1)
        assert False
    except KeyError:
        assert True

    for k, _ in I:
        h.remove(k)

    try:
        h.remove(-1)
        assert False
    except KeyError:
        assert True

    assert len(h) == 0
