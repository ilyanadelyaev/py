class Direction(object):
    def __init__(self, id_=None, name=None):
        self.id = id_
        self.name = name
        self.stations = []

    def _draw(self):
        print '=' * 10
        print '| {} [{}]'.format(self.name, self.id)
        print '-' * 4
        for i, s in enumerate(self.stations):
            print 'o {}'.format(s)
            if i < len(self.stations)-1:
                print '|'
        print '=' * 10


class Directions(object):
    def _test_create(self, stations):
        for i in xrange(2):
            name = 'Direction {}'.format(i)
            self.create(name)
        for i in sorted(self.directions):
            d = self.directions[i]
            prev_id = None
            for j in sorted(stations.stations):
                s = stations.stations[j]
                self.add_station(d.id, s.id, prev_id)
                prev_id = s.id
        self.directions[1].stations.reverse()

    def _draw(self):
        for k in sorted(self.directions):
            self.directions[k]._draw()

    def __init__(self):
        self.directions = {}

    def create(self, name):
        id_ = len(self.directions)
        d = Direction(id_, name)
        self.directions[id_] = d
        return d

    def add_station(self, directon_id, station_id, insert_after_id):
        if not self.get_by_id(directon_id):
            raise Exception('Direction with id [{}] not exists'.format(name))
        if insert_after_id is None:
            i = 0
        else:
            i = self.directions[directon_id].stations.index(insert_after_id) + 1
        self.directions[directon_id].stations.insert(i, station_id)

    def get_raw_route(self, direction_id, begin_station_id, end_station_id):
        if begin_station_id == end_station_id:
            raise Exception('begin_station_id == end_station_id')
        d = self.get_by_id(direction_id)
        if not d:
            raise Exception('Direction with id [{}] not exists'.format(name))
        if begin_station_id in d.stations and end_station_id in d.stations:
            i = d.stations.index(begin_station_id)
            j = d.stations.index(end_station_id)
            if i > j:
                reverse = True
                i, j = j, i
            reverse = False
            ret = d.stations[i:j+1]
            if reverse:
                ret.reverse()
            return ret
        raise Exception("Can't find selected stations")

    def get_by_id(self, id_):
        return self.directions.get(id_, None)
