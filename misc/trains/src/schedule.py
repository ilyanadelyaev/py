class Schedule(object):
    def _test_create(self, routes):
        import random
        for r in routes.routes:
            wd = random.choice(range(7))
            self.add_route(wd, r)

    def _draw(self):
        print '=' * 10
        for k in sorted(self.schedule):
            s = self.schedule[k]
            print '{}: {}'.format(k, ', '.join((str(i) for i in s)))
        print '=' * 10

    def __init__(self):
        self.schedule = {}

    def add_route(self, weekday, route):
        """
        weekday:
        0 - monday
        ..
        6 - sunday
        """
        if weekday < 0 or weekday > 6:
            raise Exception('Invalid weekday: {}'.format(weekday))
        self.schedule.setdefault(weekday, set()).add(route)
