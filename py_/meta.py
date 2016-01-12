class Meta(type):
    def __new__(meta, name, bases, dct):
        print 'Meta.__new__', name
        return super(Meta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print 'Meta.__init__', name
        super(Meta, cls).__init__(name, bases, dct)


class A(object):
    __metaclass__ = Meta

    def __init__(self):
        super(A, self).__init__()
        print 'A.__init__'


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print 'B.__init__'


class C(A):
    def __init__(self):
        super(C, self).__init__()
        print 'C.__init__'


class Object(B, C):
    def __init__(self):
        super(Object, self).__init__()
        print 'Object.__init__'


Object()
