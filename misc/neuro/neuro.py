data = []

# 1
data.append(
u'010\n'
u'010\n'
u'010\n'
u'010\n'
u'010'
)

# 2
data.append(
u'111\n'
u'001\n'
u'111\n'
u'100\n'
u'111'
)

# 3
data.append(
u'111\n'
u'001\n'
u'111\n'
u'001\n'
u'111'
)

# 4

data.append(
u'101\n'
u'101\n'
u'111\n'
u'001\n'
u'001'
)

# 6

data.append(
u'111\n'
u'100\n'
u'111\n'
u'101\n'
u'111'
)

# 7

data.append(
u'111\n'
u'001\n'
u'001\n'
u'010\n'
u'010'
)

# 8

data.append(
u'111\n'
u'101\n'
u'111\n'
u'101\n'
u'111'
)

# 9

data.append(
u'111\n'
u'101\n'
u'111\n'
u'001\n'
u'010'
)

# 0

data.append(
u'111\n'
u'101\n'
u'101\n'
u'101\n'
u'111'
)

# 5 - 1

data.append(
u'111\n'
u'100\n'
u'111\n'
u'001\n'
u'111'
)

# 5 - 2

data.append(
u'110\n'
u'100\n'
u'111\n'
u'001\n'
u'111'
)

# 5 - 3

data.append(
u'111\n'
u'100\n'
u'111\n'
u'001\n'
u'011'
)

# 5 - 4

data.append(
u'110\n'
u'100\n'
u'111\n'
u'001\n'
u'011'
)

# 5 - 5

data.append(
u'111\n'
u'100\n'
u'110\n'
u'001\n'
u'111'
)

# 5 - 6

data.append(
u'111\n'
u'100\n'
u'011\n'
u'001\n'
u'111'
)

# 5 - 7

data.append(
u'111\n'
u'100\n'
u'010\n'
u'001\n'
u'111'
)

# 5 - 8

data.append(
u'011\n'
u'100\n'
u'111\n'
u'001\n'
u'111'
)

# 5 - 9

data.append(
u'111\n'
u'100\n'
u'111\n'
u'001\n'
u'110'
)

# 5 - 10

data.append(
u'011\n'
u'100\n'
u'111\n'
u'001\n'
u'110'
)

# 5 - 11

data.append(
u'111\n'
u'100\n'
u'110\n'
u'001\n'
u'110'
)

printable_data = data[:]
for i in xrange(len(data)):
    t = data[i].replace(u'0', u' ')
    t = t.replace(u'1', u'\u2588')
    data[i] = data[i].replace('\n', ''), t

#for d in data:
#    print d[1]
#    print d[0]



class Neuro(object):
    def __init__(self):
        self.weight = [0.0] * (5 * 3)  # link weight
        self.limit = 9  # responce limit

    def process(self, data):
        mul = []
        # multiply signal to link weight
        for i in xrange(5):
            for j in xrange(3):
                p = i * 3 + j
                mul.append(int(data[p]) * self.weight[p])
        # sum signals
        sm = sum(mul)

        return sm >= self.limit, sm

    def inc_weight(self, data):
        for i in xrange(5):
            for j in xrange(3):
                p = i * 3 + j
                self.weight[p] += int(data[p])

    def dec_weight(self, data):
        for i in xrange(5):
            for j in xrange(3):
                p = i * 3 + j
                self.weight[p] -= int(data[p])

    def save(self):
        import zlib
        import json
        with open('./neuro.dat', 'wb') as f:
            f.write(zlib.compress(json.dumps(self.weight)))
            print 'weight has saved'

    def load(self):
        import zlib
        import json
        try:
            with open('./neuro.dat', 'rb') as f:
                self.weight = json.loads(zlib.decompress(f.read()))
            print 'weight has loaded'
        except IOError:
            pass


if __name__ == '__main__':
    n = Neuro()
    n.load()

    def process(n, educate=False):
        for d, v in data:
            print v
            res = n.process(d)
            print res[0], res[1]
            if not educate:
                continue
            print 'T (true) / F (false) / S (skip)'
            while True:
                ans = raw_input()
                ans = ans.lower()
                if ans == 's':
                    break
                if ans == 't':
                    if not res[0]:
                        print 'increase'
                        n.inc_weight(d)
                    break
                elif ans == 'f':
                    if res[0]:
                        print 'decrease'
                        n.dec_weight(d)
                    break
                else:
                    print 'invalid. try again'
                    continue

    #process(n, educate=True)
    # [0.0, 1.0, 0.0, 5.0, 0.0, -7.0, 0.0, 0.0, 0.0, -11.0, 0.0, 1.0, 1.0, 1.0, 1.0]

    process(n)

    print n.weight

    n.save()
