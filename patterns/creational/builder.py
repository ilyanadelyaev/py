class Infantryman(object):
    def act(self):
        print 'hack'


class Archer(object):
    def act(self):
        print 'fire'


####################


class Army(object):
    def __init__(self, name):
        self.name = name
        self.infantry = []
        self.archers = []

    def make_turn(self):
        print self.name
        for i in self.infantry:
            i.act()
        for a in self.archers:
            a.act()


####################


class ArmyBuilder(object):
    def __init__(self):
        self.army = None

    def build_infantry(self):
        raise NotImplementedError

    def build_archers(self):
        raise NotImplementedError

    def get_army(self):
        return self.army


##########


class A_ArmyBuilder(ArmyBuilder):
    def __init__(self):
        super(A_ArmyBuilder, self).__init__()

    def create_army(self):
        self.army = Army('A army')

    def build_infantry(self):
        for _ in xrange(1):
            self.army.infantry.append(Infantryman())

    def build_archers(self):
        for _ in xrange(3):
            self.army.archers.append(Archer())


##########


class B_ArmyBuilder(ArmyBuilder):
    def __init__(self):
        super(B_ArmyBuilder, self).__init__()

    def create_army(self):
        self.army = Army('B army')

    def build_infantry(self):
        for _ in xrange(3):
            self.army.infantry.append(Infantryman())

    def build_archers(self):
        for _ in xrange(1):
            self.army.archers.append(Archer())


####################


class Director(object):
    def create_army(self, builder):
        builder.create_army()
        builder.build_infantry()
        builder.build_archers()
        return builder.get_army()


####################


if __name__ == '__main__':
    d = Director()

    a_builder = A_ArmyBuilder()
    b_builder = B_ArmyBuilder()

    #

    a_army = d.create_army(a_builder)
    b_army = d.create_army(b_builder)

    #

    a_army.make_turn()
    b_army.make_turn()
