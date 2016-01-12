class Route(object):
    def __init__(self, id_, name, direction, route):
        self.id = id_
        self.name = name
        self.direction = direction
        self.route = route

    def _draw(self):
        print '=' * 10
        print '+ {} [{}]'.format(self.name, self.direction)
        print '-' * 10
        for i, r in enumerate(self.route):
            print '* {}'.format(r)
            if i < len(self.route)-1:
                print '+'
        print '=' * 10


class Routes(object):
    def _test_create(self, stations, directions):
        import random
        st = stations.stations.keys()
        dr = directions.directions.keys()
        for i in xrange(5):
            d = random.choice(dr)
            begin = random.choice(st)
            end = random.choice(st)
            if begin == end:
                continue
            rr = directions.get_raw_route(d, begin, end)
            self.create('Route {}'.format(i), d, rr)

    def _draw(self):
        for k in sorted(self.routes):
            self.routes[k]._draw()

    def __init__(self):
        self.routes = {}

    def create(self, name, direction, raw_route):
        id_ = len(self.routes)
        r = Route(id_, name, direction, raw_route)
        self.routes[id_] = r
        return r
