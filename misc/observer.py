class Observer(object):
    def __init__(self, **kwargs):
        self.attrs_dict = kwargs

    def __getattr__(self, key):
        if key not in self.attrs_dict:
            raise KeyError
        return self.attrs_dict.get(key)

    def __repr__(self):
        attrs = [(k, v) for k, v in self.attrs_dict.iteritems() if not k.startswith('_')]
        return '{}({})'.format(self.__class__.__name__, ', '.join('{}={}'.format(k, v) for k, v in attrs))


class X(Observer):
    pass

x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))

print x

assert x.foo == 1
assert x.name == 'Amok'
assert x._bazz == 12
