class Base_1(object):
    def __init__(self):
        super(Base_1, self).__init__()
        print 'Base_1.__init__'

    def f(self):
        print 'Base_1.f'


class Base_2(object):
    def __init__(self):
        super(Base_2, self).__init__()
        print 'Base_2.__init__'

    def f(self):
        print 'Base_2.f'


class Impl_1_1(Base_1):
    def __init__(self):
        super(Impl_1_1, self).__init__()
        print 'Impl_1_1.__init__'

    #def f(self):
    #    print 'Impl_1_1.f'


class Impl_1_2(Base_1):
    def __init__(self):
        super(Impl_1_2, self).__init__()
        print 'Impl_1_2.__init__'

    #def f(self):
    #    print 'Impl_1_2.f'


class Impl_2_1(Base_2):
    def __init__(self):
        super(Impl_2_1, self).__init__()
        print 'Impl_2_1.__init__'

    def f(self):
        print 'Impl_2_1.f'


class Object(Impl_1_1, Impl_1_2, Impl_2_1):
    def __init__(self):
        super(Object, self).__init__()
        print 'Object.__init__'

    def f(self):
        super(Object, self).f()
        #print 'Object.f'


print 'Object(Impl_1_1(Base_1), Impl_1_2(Base_1), Impl_2_1(Base_2))'
o = Object()

o.f()

print Object.__mro__
print Object.mro()


print '=' * 10


class X(object):
#class X:
    def x(self):
        print 'x'
    def y(self):
        print 'y'
    def z(self):
        print 'z'

class Y(X):
    def x(self):
        print 'y.x'
    def y(self):
        print 'y.y'

class Z(X):
    def x(self):
        print 'z.x'
    def z(self):
        print 'z.z'
    def z_z(self):
        print 'z_z'

#class W(Y, Z):
class W(Z, Y):
    pass

w = W()
w.x()
w.y()
w.z()
w.z_z()
