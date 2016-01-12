class Station(object):
    def __init__(self, id_, name, hub=False):
        self.id = id_
        self.name = name
        self.hub = hub

    def _draw(self):
        print 'o {} [{}]'.format(self.name, self.id)


class Stations(object):
    def _test_create(self):
        for i in xrange(10):
            name = 'Station {}'.format(i)
            self.create(name)

    def _draw(self):
        print '=' * 10
        for k in sorted(self.stations):
            self.stations[k]._draw()
        print '=' * 10

    def __init__(self):
        self.stations = {}

    def create(self, name):
        id_ = len(self.stations)
        s = Station(id_, name)
        self.stations[id_] = s
        return s

    def get_by_id(self, id_):
        return self.stations.get(id_, None)
