class Unit(object):
    def get_strength(self):
        raise NotImplementedError

    def add_unit(self, unit):
        raise NotImplementedError


class Infantryman(Unit):
    def get_strength(self):
        return 2


class Archer(Unit):
    def get_strength(self):
        return 1


class CompositeUnit(Unit):
    def __init__(self):
        self.units = []

    def get_strength(self):
        return sum((u.get_strength() for u in self.units))

    def add_unit(self, unit):
        self.units.append(unit)


def create_legion():
    legion = CompositeUnit()
    #
    for _ in xrange(3000):
        legion.add_unit(Infantryman())
    #
    for _ in xrange(1200):
        legion.add_unit(Archer())
    #
    return legion


if __name__ == '__main__':
    army = CompositeUnit()
    for _ in xrange(4):
        army.add_unit(create_legion())

    print army.get_strength()
