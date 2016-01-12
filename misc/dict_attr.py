class DictAttr(dict):
    def __getattr__(self, key):
        try:
            return self.__getitem__(key)
        except KeyError as ex:
            raise AttributeError(ex)


x = DictAttr([('one', 1), ('two', 2), ('three', 3)])

print x

assert x['three'] == 3
assert x.get('one') == 1
assert x.get('five', 'missing') == 'missing'

assert x.one == 1
try:
    x.five
    assert 0
except AttributeError:
    assert 1
