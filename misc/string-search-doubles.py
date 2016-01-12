import random


def search_doubles(S):
    if len(S) < 2:
        return
    ret = []
    for i in xrange(len(S)-1):
        for j in xrange(i+1, len(S)):
            if S[i] == S[j]:
                ret.append((i, j))
                break
    return ret


def generate_random_string(length):
    src = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for _ in xrange(length):
        ret += random.choice(src)
    return ret


print 'aa', search_doubles('aa')


for _ in xrange(10):
    s = generate_random_string(20)
    print s, search_doubles(s)
