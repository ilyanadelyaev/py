class Warrior(object):
    __registry = {}

    @classmethod
    def add_proto(cls, t, proto):
        cls.__registry[t] = proto

    @classmethod
    def del_proto(cls, t):
        del cls.__registry[t]

    @classmethod
    def create_warrior(cls, t):
        return cls.__registry[t]._clone()

    def _clone(self):
        return self.__class__(self)

    def act(self):
        raise NotImplementedError


##########


class Infantryman(Warrior):
    def __init__(self, proto=None):
        # only clone
        if proto and not isinstance(proto, self.__class__):
            raise NotImplementedError
        #
        super(Infantryman, self).__init__()
        #
        if proto is None:
            self.state = 'proto'
        else:
            self.state = 'clone'

    def act(self):
        if self.state == 'proto':
            raise NotImplementedError
        print 'hack'


class Archer(Warrior):
    def __init__(self, proto=None):
        # only clone
        if proto and not isinstance(proto, self.__class__):
            raise NotImplementedError
        #
        super(Archer, self).__init__()
        #
        if proto is None:
            self.state = 'proto'
        else:
            self.state = 'clone'

    def act(self):
        if self.state == 'proto':
            raise NotImplementedError
        print 'fire'


##########


Warrior.add_proto('infantryman', Infantryman())
Warrior.add_proto('archer', Archer())


####################


class WarFactory(object):
    __registry = {
        'infantryman': Infantryman(),
        'archer': Archer(),
    }

    @classmethod
    def _create(cls, t):
        return cls.__registry[t]._clone()

    @classmethod
    def create_infantryman(cls):
        return cls._create('infantryman')

    @classmethod
    def create_archer(cls):
        return cls._create('archer')


####################


if __name__ == '__main__':
    i = Infantryman()
    try:
        i.act()
    except NotImplementedError:
        print 'proto'

    #

    i = Warrior.create_warrior('infantryman')
    a = Warrior.create_warrior('archer')

    i.act()
    a.act()

    #

    i = WarFactory.create_infantryman()
    a = WarFactory.create_archer()

    i.act()
    a.act()
