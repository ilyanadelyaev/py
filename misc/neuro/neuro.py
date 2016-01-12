import os


IMG_SIZE_X = 3
IMG_SIZE_Y = 5


class Neuro(object):
    def __init__(self):
        self.weight = [0] * (IMG_SIZE_X * IMG_SIZE_Y)  # link weight
        self.limit = int(float(IMG_SIZE_X * IMG_SIZE_Y) * 0.65)  # responce limit

    def process(self, seq):
        mul = []
        # multiply signal to link weight
        for i in xrange(IMG_SIZE_Y):
            for j in xrange(IMG_SIZE_X):
                p = i * IMG_SIZE_X + j
                mul.append(int(seq[p]) * self.weight[p])
        # sum signals
        sm = sum(mul)

        return sm >= self.limit, sm

    def inc_weight(self, seq):
        for i in xrange(IMG_SIZE_Y):
            for j in xrange(IMG_SIZE_X):
                p = i * IMG_SIZE_X + j
                self.weight[p] += int(seq[p])

    def dec_weight(self, seq):
        for i in xrange(IMG_SIZE_Y):
            for j in xrange(IMG_SIZE_X):
                p = i * IMG_SIZE_X + j
                self.weight[p] -= int(seq[p])


def read_image(path):
    with open(path, 'rb') as f:
        rep = f.read().decode('utf8').strip('\n')
        seq = rep.replace(u'\u2588', u'1')
        seq = seq.replace(u' ', u'0')
        seq = seq.replace('\n', '')
        return rep, seq


if __name__ == '__main__':
    # load numbers

    numbers = []
    for num in xrange(10):
        numbers.append([])
        for var in xrange(10):
            path = os.path.join(os.path.dirname(__file__), 'numbers', str(num), str(var))
            if os.path.exists(path):
                rep, seq = read_image(path)
                numbers[num].append((rep, seq))

    # create neuros

    neuros = [Neuro() for _ in xrange(10)]

    # learn

    for neuro_i, neuro in enumerate(neuros):

        # TODO: have problems with 8
        if neuro_i == 8:
            continue

        while True:
            corrected = False

            for num_i, num in enumerate(numbers):

                for _, seq in num:

                    res = neuro.process(seq)

                    # increase for correct number
                    if (neuro_i == num_i) and not res[0]:
                        neuro.inc_weight(seq)
                        corrected = True

                    # decrease for incorrect number
                    elif not (neuro_i == num_i) and res[0]:
                        neuro.dec_weight(seq)
                        corrected = True

            if not corrected:
                break

    # show results

    for neuro_i, neuro in enumerate(neuros):
        print neuro.weight

    # check

    while True:
        print 'Print number image like: 0/1'
        print 'Empty for break'
        print '>',
        inp = raw_input()
        if not inp:
            break
        path = os.path.join(os.path.dirname(__file__), 'numbers', inp)
        if os.path.exists(path):
            rep, seq = read_image(path)
            print rep
            res = []
            for neuro_i, neuro in enumerate(neuros):
                ret, val = neuro.process(seq)
                res.append(ret)
            if sum(res) != 1:
                print '!! Ivalid neuro state with:', res
            else:
                print 'Number is:', res.index(1)
        else:
            print '!! Invalid image. Try again..'
