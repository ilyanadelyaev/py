def printable(func):
    def decoy(*args, **kwargs):
        val = func(*args, **kwargs)
        print val
        return val
    return decoy

@printable
def f(val):
    return val

a = f(5)
print a + 1


##########
print '=' * 10
##########


def appendix(prefix):
    def functor(func):
        def decoy(*args, **kwargs):
            return prefix + func(*args, **kwargs)
        return decoy
    return functor

class A(object):
    def __repr__(self):
        return 'A class'

    @appendix('super')
    def f(self):
        return str(self)

print A().f()


##########
print '=' * 10
##########


def singleton(cls):
    instances = dict()
    def decoy(*args, **kwagrs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwagrs)
        return instances.get(cls)
    return decoy

@singleton
class A(object):
    pass

a1 = A()
a2 = A()
print id(a1) == id(a2)


##########
print '=' * 10
##########


def applier(key, value):
    def classifier(cls):
        setattr(cls, key, value)
        def decoy(*args, **kwagrs):
            return cls(*args, **kwagrs)
        return decoy
    return classifier

@applier('key', 'value')
class A(object):
    pass

print A().key
