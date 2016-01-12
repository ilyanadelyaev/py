# Minimal portable random generator by Park and Miller

# Lewis-Goodman-Miller constants
IA = 16807
IM = 2147483647
AM = 1.0 / IM

# Scharge constants
IQ = 12773
IR = 2836

# Special mask to be explained below
MASK = 123456789


# initial seed, for all the generators here
_dummy = 0

def seed(d):
    _dummy = d


# returns random uniformly distributed between 0 and 1
def unirand0():
    global _dummy

    _dummy ^= MASK  # avoid (_dummy == 0)

    k = _dummy / IQ

    _dummy = IA * ( _dummy - k * IQ ) - IR * k
    if _dummy < 0:
        _dummy += IM

    ans = AM * _dummy

    _dummy ^= MASK  # restore unmasked _dummy

    return ans


# Minimal random generator with Bays-Durham shuffle

NTAB = 32
NWUP = 8
NDIV = 1 + ( IM - 1 ) / NTAB
EPS = 1.2e-7
RNMX = 1.0 - EPS


_iy = 0
_iv = [0] * NTAB

def unirand1():
    global _dummy
    global _iy
    global _iv

    # initialize
    if _dummy <= 0 or not _iy:
        # avoid negative or zero seed
        if _dummy < 0:
            _dummy = -_dummy
        elif _dummy == 0:
            _dummy = 1

        # after NWUP warmups, initialize shuffle table
        j = NTAB + NWUP - 1
        while j >= 0:
            k = _dummy / IQ
            _dummy = IA * ( _dummy - k * IQ ) - IR * k
            if _dummy < 0:
                _dummy += IM
            if j < NTAB:
                _iv[j] = _dummy
            j -= 1

        # first specimen from the table
        _iy = _iv[0]

    # regular work: generate new number
    k = _dummy / IQ;
    _dummy = IA * ( _dummy - k * IQ ) - IR * k
    if _dummy < 0:
        _dummy += IM

    # shuffle output
    i = _iy / NDIV
    _iy = _iv[i]
    _iv[i] = _dummy

    temp = AM * _iy
    if temp > RNMX:
        temp = RNMX

    return temp


if __name__ == '__main__':
    import time
    import random

    attempts = 100000

    random.seed(time.time())
    t = [random.random() for _ in xrange(attempts)]
    print 'python random:', sum(t) / len(t)

    seed(time.time())
    t = [unirand0() for _ in xrange(attempts)]
    print 'unirand0:', sum(t) / len(t)

    seed(time.time())
    t = [unirand1() for _ in xrange(attempts)]
    print 'unirand1:', sum(t) / len(t)
