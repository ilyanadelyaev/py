import json
import zlib


class Memento(object):
    def __init__(self, data):
        self.data = zlib.compress(json.dumps(data))

    def get_data(self):
        return json.loads(zlib.decompress(self.data))


class Object(object):
    def __init__(self, state):
        self.state = state

    def __repr__(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def save(self):
        return Memento({
            'state': self.state,
        })

    def restore(self, memento):
        data = memento.get_data()
        self.state = data.get('state', None)


if __name__ == '__main__':
    obj = Object('one')
    print obj

    mm = obj.save()

    obj.set_state('two')
    print obj

    obj.restore(mm)
    print obj
