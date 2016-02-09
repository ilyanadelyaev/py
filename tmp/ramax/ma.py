class MyError(Exception):
    pass


class Parent(object):
    def __init__(self, i):
        self.i = i

    def fnc(self, val_1, val_2=None):
        if val_1 == 7:
            raise MyError('Error text')
        if val_2 is None:
            val_2 = val_1
        return val_1 * val_2 * self.i


class First(Parent):
    def __init__(self, *args, **kwargs):
        super(Second, self).__init__(*args, **kwargs)
        #
        self.first_value = None

    def isFirst(self):
        if self.first_value is None:
            raise NotImplementedError
        return self.first_value


class Second(Parent):
    def __init__(self, *args, **kwargs):
        super(Second, self).__init__(*args, **kwargs)
        #
        self.second_value = None

    @property
    def isSecond(self):
        if self.second_value is None:
            raise NotImplementedError
        return self.second_value


class A(First, Second):
    def __init__(self):
        super(A, self).__init__(i=3)
        #
        self.first_value = 1
        self.second_value = 0
