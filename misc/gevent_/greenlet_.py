from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
print 'main'


print '=' * 10


def func1(i):
    print gr2.switch(2)
    return i

def func2(i):
    return i

gr1 = greenlet(func1)
gr2 = greenlet(func2)
print gr1.switch(1)
print 'main 1'
print gr1.switch(10)
print 'main 2'
