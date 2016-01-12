class Swimming(object):
    def swim(self):
        raise NotImplementedError


class FreestyleSwimming(Swimming):
    def swim(self):
        return 'FREESTYLE'


class ButterflySwimming(Swimming):
    def swim(self):
        return 'BUTTERFLY'


class BrassSwimming(Swimming):
    def swim(self):
        return 'BRASS'


class Swimmer(object):
    def __init__(self):
        self.style = 'brass'
        self.freestyle_swimming = FreestyleSwimming()
        self.butterfly_swimming = ButterflySwimming()
        self.brass_swimming = BrassSwimming()

    def _swimming(self):
        if self.style == 'brass':
            return self.brass_swimming
        elif self.style == 'butterfly':
            return self.butterfly_swimming
        return self.freestyle_swimming

    def make_freestyle(self):
        self.style = 'freestyle'

    def make_butterfly(self):
        self.style = 'butterfly'

    def make_brass(self):
        self.style = 'brass'

    def swim(self):
        print self._swimming().swim()


if __name__ == '__main__':
    s = Swimmer()

    s.swim()

    s.make_freestyle()
    s.swim()

    s.make_butterfly()
    s.swim()
