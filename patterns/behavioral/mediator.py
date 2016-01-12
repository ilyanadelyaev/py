class ControlTower(object):
    def __init__(self):
        self.runway_state = 'empty'

    def request_takeoff(self):
        if self.runway_state == 'empty':
            self.runway_state = 'request_takeoff'
            return True
        return False

    def request_landing(self):
        if self.runway_state == 'empty':
            self.runway_state = 'request_landing'
            return True
        return False

    def make_turn(self):
        print '...'
        if self.runway_state == 'request_takeoff':
            self.runway_state = 'takeoff'
        elif self.runway_state == 'takeoff':
            self.runway_state = 'empty'
        elif self.runway_state == 'request_landing':
            self.runway_state = 'landing'
        elif self.runway_state == 'landing':
            self.runway_state = 'empty'


class Airplane(object):
    def __init__(self, id_, control_tower):
        self.control_tower = control_tower
        self.id = id_
        self.state = 'land'

    def request_takeoff(self):
        print self.id, 'request_takeoff',
        ret = self.control_tower.request_takeoff()
        if ret:
            self.state = 'air'
        print self.state

    def request_landing(self):
        print self.id, 'request_landing',
        ret = self.control_tower.request_landing()
        if ret:
            self.state = 'land'
        print self.state


if __name__ == '__main__':
    ct = ControlTower()

    a1 = Airplane('one', ct)
    a2 = Airplane('two', ct)

    a1.request_takeoff()
    a2.request_takeoff()
    ct.make_turn()
    a2.request_takeoff()
    ct.make_turn()
    a2.request_takeoff()
    ct.make_turn()
    a2.request_landing()
    a1.request_landing()
    ct.make_turn()
    a2.request_landing()
    a1.request_landing()
