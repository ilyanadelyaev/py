class Warrior(object):
    def info(self):
        return self.__class__.__name__


class Infantryman(Warrior):
    pass


class Archer(Warrior):
    pass


####################


def factory(t):
    if t == 'infantryman':
        return Infantryman()
    elif t == 'archer':
        return Archer()


####################


class WarriorsFactory(object):
    def create_warrior(self):
        raise NotImplementedError


class InfantryFactory(WarriorsFactory):
    def create_warrior(self):
        return Infantryman()


class ArchersFactory(WarriorsFactory):
    def create_warrior(self):
        return Archer()


####################


if __name__ == '__main__':
    i = factory('infantryman')
    a = factory('archer')

    print i.info()
    print a.info()

    #

    i_f = InfantryFactory()
    a_f = ArchersFactory()

    i = i_f.create_warrior()
    a = a_f.create_warrior()

    print i.info()
    print a.info()
