def select_sort(I):
    I = I[::]
    N = len(I)
    for i in xrange(N-1):
        m = I[i]
        c = i
        for j in xrange(i, N):
            if m > I[j]:
                m = I[j]
                c = j
        t = I[i]
        I[i] = m
        I[c] = t
    return I


def bubble_sort(I):
    I = I[::]
    N = len(I)
    for i in xrange(N-2):
        for j in xrange(N-1, i, -1):
            if I[j] < I[j-1]:
                t = I[j-1]
                I[j-1] = I[j]
                I[j] = t
    return I


def insert_sort(I):
    I = I[::]
    N = len(I)
    for i in xrange(1, N):
        for j in xrange(i, 0, -1):
            if I[j] < I[j-1]:
                t = I[j-1]
                I[j-1] = I[j]
                I[j] = t
            else:
                break
    return I


def pyramid_sort(I):
    I = I[::]
    N = len(I)
    #import pdb; pdb.set_trace()
    for i in xrange(N/2, 0-1, -1):
        if 2*i+1 >= N:
            continue
        li = 2*i+1
        ri = 2*i+2
        if ri >= N:
            ri = i
        l = I[li]
        r = I[ri]
        if r > l:
            mi = ri
        else:
            mi = li
        if I[i] < I[mi]:
            t = I[i]
            I[i] = I[mi]
            I[mi] = t
    return I


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    import random
    #N = 2**14
    N = 10
    I = random.sample(xrange(N**3), N)
    I = [44, 55, 12, 42, 94, 18, 6, 67]
    print I

    #import cProfile
    #print 'SYSTEM'
    #cProfile.run('sorted(I)')
    #print 'SELECT'
    #cProfile.run('select_sort(I)')
    #print 'BUBBLE'
    #cProfile.run('bubble_sort(I)')
    #print 'INSERT'
    #cProfile.run('insert_sort(I)')

    #if sorted(I) != select_sort(I):
    #    print 'ERROR!!'
    #if sorted(I) != bubble_sort(I):
    #    print "ERROR!!"
    #if sorted(I) != insert_sort(I):
    #    print "ERROR!!"

    print sorted(I)
    #print select_sort(I)
    #print bubble_sort(I)
    #print insert_sort(I)
    print pyramid_sort(I)
