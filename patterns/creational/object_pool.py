class ObjectPool(object):
    def __init__(self, limit):
        self.objects = {}
        self.limit = limit

    def accure(self):
        if len(self.objects) >= self.limit:
            return None
        obj = Object()
        self.objects[obj.id] = obj
        return obj

    def release(self, obj):
        del self.objects[obj.id]

    def get(self, id):
        return self.objects.get(id, None)


class Object(object):
    def __init__(self):
        self.id = id(self)

    def __repr__(self):
        return 'Object_{}'.format(self.id)


if __name__ == '__main__':
    pool = ObjectPool(2)

    o1 = pool.accure()
    o2 = pool.accure()

    assert pool.accure() == None

    pool.release(o1)

    assert pool.get(o1.id) == None
    o1 = None

    o3 = pool.accure()

    print o1, o2, o3
