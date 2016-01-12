print 'pre Meta'
class Meta(type):
    def __new__(cls, *args, **kw):
        print 'Meta.__new__', args, kw
        return super(Meta, cls).__new__(cls, *args, **kw)
    def __init__(cls, *args, **kw):
        print 'Meta.__init__', args, kw
        return super(Meta, cls).__init__(*args, **kw)
    def __call__(cls, *args, **kw):
        print 'Meta.__call__', args, kw
        #return super(Meta, cls).__call__(*args, **kw)
print 'post Meta'


print 'pre A'
class A(object):
    __metaclass__ = Meta
    def __new__(cls, *args, **kw):
        print 'A.__new__', args, kw
        return super(A, cls).__new__(cls, *args, **kw)
    def __init__(self, var):
        print 'A.__init__'
        self.var = var
print 'post A'


if __name__ == '__main__':
    print 'create A'
    a = A(1)
    print 'done A'
