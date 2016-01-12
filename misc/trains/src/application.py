import stations
import directions
import routes
import schedule


class Application(object):
    def __init__(self):
        self.stations = stations.Stations()
        self.directions = directions.Directions()
        self.routes = routes.Routes()
        self.schedule = schedule.Schedule()

        # test
        self.stations._test_create()
        self.stations._draw()
        self.directions._test_create(self.stations)
        self.directions._draw()
        self.routes._test_create(self.stations, self.directions)
        self.routes._draw()
        self.schedule._test_create(self.routes)
        self.schedule._draw()
