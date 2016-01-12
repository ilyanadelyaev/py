class Infantryman(object):
    def act(self):
        raise NotImplementedError


class Archer(object):
    def act(self):
        raise NotImplementedError


##########


class A_Infantryman(Infantryman):
    def act(self):
        return 'hach like A'


class A_Archer(Archer):
    def act(self):
        return 'fire like A'


##########


class B_Infantryman(Infantryman):
    def act(self):
        return 'hach like B'


class B_Archer(Archer):
    def act(self):
        return 'fire like B'


####################


class WarFactory(object):
    def create_infantryman(self):
        raise NotImplementedError

    def create_archer(self):
        raise NotImplementedError


##########


class A_WarFactory(WarFactory):
    def create_infantryman(self):
        return A_Infantryman()

    def create_archer(self):
        return A_Archer()


##########


class B_WarFactory(WarFactory):
    def create_infantryman(self):
        return B_Infantryman()

    def create_archer(self):
        return B_Archer()


####################


class Army(object):
    def __init__(self):
        self.factory = None
        self.infantry = []
        self.archers = []

    def create_army(self):
        for _ in xrange(2):
            self.infantry.append(self.factory.create_infantryman())
        for _ in xrange(2):
            self.archers.append(self.factory.create_archer())

    def make_turn(self):
        print self.__class__.__name__
        for i in self.infantry:
            print i.act()
        for a in self.archers:
            print a.act()


##########


class A_Army(Army):
    def __init__(self):
        super(A_Army, self).__init__()
        self.factory = A_WarFactory()


##########


class B_Army(Army):
    def __init__(self):
        super(B_Army, self).__init__()
        self.factory = B_WarFactory()


####################


if __name__ == '__main__':
    armies = [A_Army(), B_Army()]

    for a in armies:
        a.create_army()

    for a in armies:
        a.make_turn()
