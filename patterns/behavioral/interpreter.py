import random


class Pattern(object):
    def interpret(self, val):
        for num, var in sorted(self.variants, key=lambda x: x[0], reverse=True):
            ret = val.rfind(var)
            if ret != -1 and ( ret + len(var) == len(val) ):
                return val[:ret], num
        return val, 0

    def generate(self, val):
        try:
            return [v for n, v in self.variants if n == val][0]
        except IndexError:
            return ''


class Pattern_One(Pattern):
    variants = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IIII'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'VIIII'),
        (9, 'IX'),
    ]


class Pattern_Ten(Pattern):
    variants = [
        (10, 'X'),
        (20, 'XX'),
        (30, 'XXX'),
        (40, 'XXXX'),
        (40, 'XL'),
        (50, 'L'),
        (60, 'LX'),
        (70, 'LXX'),
        (80, 'LXXX'),
        (90, 'LXXXX'),
        (90, 'XC'),
    ]


class Pattern_Hundred(Pattern):
    variants = [
        (100, 'C'),
        (200, 'CC'),
        (300, 'CCC'),
        (400, 'CCCC'),
        (400, 'CD'),
        (500, 'D'),
        (600, 'DC'),
        (700, 'DCC'),
        (800, 'DCCC'),
        (900, 'DCCCC'),
        (900, 'CM'),
    ]


class Pattern_Thousand(Pattern):
    variants = [
        (1000, 'M'),
        (2000, 'MM'),
        (3000, 'MMM'),
        (4000, 'MMMM'),
    ]


class Interpreter(object):
    def __init__(self):
        self.pattern_one = Pattern_One()
        self.pattern_ten = Pattern_Ten()
        self.pattern_hundred = Pattern_Hundred()
        self.pattern_thousand = Pattern_Thousand()

    def interpret(self, val):
        val = val.upper()
        #
        val, one = self.pattern_one.interpret(val)
        val, ten = self.pattern_ten.interpret(val)
        val, hundred = self.pattern_hundred.interpret(val)
        val, thousand = self.pattern_thousand.interpret(val)
        # invalid value
        if val:
            return 0
        #
        return thousand + hundred + ten + one

    def generate(self, val):
        # invalid value
        if val < 1 or val > 4999:
            return ''
        #
        one = val % 10
        val -= one
        ten = val % 100
        val -= ten
        hundred = val % 1000
        val -= hundred
        thousand = val % 10000
        val -= thousand
        #
        one = self.pattern_one.generate(one)
        ten = self.pattern_ten.generate(ten)
        hundred = self.pattern_hundred.generate(hundred)
        thousand = self.pattern_thousand.generate(thousand)
        #
        return thousand + hundred + ten + one


if __name__ == '__main__':
    interpreter = Interpreter()

    for i in (0, 1, 10, 100, 1000, 11, 222, 3333, 4999):
        val = interpreter.generate(i)
        assert i == interpreter.interpret(val)

    for _ in xrange(100):
        i = random.randint(1, 4999)
        val = interpreter.generate(i)
        assert i == interpreter.interpret(val)

    assert interpreter.interpret('CXCX') == 0  # invalid
    assert interpreter.interpret('MCMXCVI') == 1996
    assert interpreter.interpret('MMMCMXCIX') == 3999
    assert interpreter.interpret('MMMM') == 4000
    assert interpreter.interpret('MDCLXVIIII') == 1669
    assert interpreter.interpret('MDCLXVI') == 1666
    assert interpreter.interpret('DCCCLXXXVIII') == 888
    assert interpreter.interpret('MMMMCMXCIX') == 4999
