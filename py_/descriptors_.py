class Descriptor(object):
    def __init__(self, value):
        self.value = value
        self.val_type = type(value)

    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, value):
        if not isinstance(value, self.val_type):
            raise TypeError
        self.value = value


class Meta(type):
    def __new__(meta, name, bases, dct):
        for k in dct:
            if k.startswith('_'):
                continue
            dct[k] = Descriptor(dct[k])
        return super(Meta, meta).__new__(meta, name, bases, dct)


class Object(object):
    __metaclass__ = Meta
    int_value = 0
    str_value = ''


obj = Object()

obj.int_value = 5
print obj.int_value
try:
    obj.int_value = 'a'
except TypeError:
    print 'TypeError'

obj.str_value = 'a'
print obj.str_value
try:
    obj.str_value = 5
except TypeError:
    print 'TypeError'
