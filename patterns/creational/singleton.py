print 'pre Meta'
class Meta(type):
    def __new__(cls, *args, **kw):
        print 'Meta.__new__', cls, args, kw
        return super(Meta, cls).__new__(cls, *args, **kw)
    def __init__(cls, *args, **kw):
        print 'Meta.__init__', cls, args, kw
        return super(Meta, cls).__init__(*args, **kw)
    def __call__(cls, *args, **kw):
        print 'Meta.__call__', cls, args, kw
        return super(Meta, cls).__call__(*args, **kw)
print 'post Meta'


print 'pre A'
class A(object):
    __metaclass__ = Meta
    __instance = None
    def __new__(cls, *args, **kw):
        print 'A.__new__', cls, args, kw
        if cls.__instance is None:
            cls.__instance = super(A, cls).__new__(cls, *args, **kw)
        return cls.__instance
    def __init__(self):
        print 'A.__init__', self
print 'post A'


if __name__ == '__main__':
    print 'create A'
    a = A()
    print 'done A'

    assert id(A()) == id(A())
