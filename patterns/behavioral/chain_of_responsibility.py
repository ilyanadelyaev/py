import random
import pprint


class Handler_1(object):
    def __init__(self, storage):
        self._storage = storage

    def handle(self, val):
        if val >= 0 and val <= 9:
            self._storage.setdefault(1, []).append(val)
            return True


class Handler_10(object):
    def __init__(self, storage):
        self._storage = storage

    def handle(self, val):
        if val >= 10 and val <= 99:
            self._storage.setdefault(10, []).append(val)
            return True


class Processor(object):
    def __init__(self):
        self._storage = {}
        self.handlers = [
            Handler_1(self._storage),
            Handler_10(self._storage),
        ]

    def handle_stack(self, stack):
        for i in stack:
            processed = False
            for h in self.handlers:
                if h.handle(i):
                    processed = True
                    break
            if not processed:
                self._storage.setdefault(0, []).append(i)

    def get_storage(self):
        return self._storage


if __name__ == '__main__':
    p = Processor()

    stack = [random.randint(0, 200) for _ in xrange(20)]
    p.handle_stack(stack)

    s = p.get_storage()
    pprint.pprint(p.get_storage())
