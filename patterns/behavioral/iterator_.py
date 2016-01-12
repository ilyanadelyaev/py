class Object(object):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data


class Container(object):
    def get(self, pos):
        raise NotImplementedError

    def length(self):
        raise NotImplementedError


class ListContainer(Container):
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def get(self, pos):
        return self.objects[pos]

    def length(self):
        return len(self.objects)


class Iterator(object):
    def __init__(self, container):
        self.pos = 0
        self.container = container

    def next(self):
        if self.pos >= self.container.length():
            raise StopIteration
        o = self.container.get(self.pos)
        self.pos += 1
        return o


if __name__ == '__main__':
    c = ListContainer()

    c.add(Object('a'))
    c.add(Object('b'))
    c.add(Object('c'))

    i = Iterator(c)

    print i.next()
    print i.next()
    print i.next()
    try:
        i.next()
    except StopIteration:
        print 'StopIteration'
