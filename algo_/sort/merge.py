def merge_sort(D, reverse=False):
    if len(D) == 1:
        return D

    md = len(D) / 2

    L = merge_sort(D[:md], reverse=reverse)
    R = merge_sort(D[md:], reverse=reverse)

    DD = []

    for _ in xrange(len(D)):
        if L[0] > R[0] if reverse else L[0] < R[0]:
            DD.append(L[0])
            del L[0]
        else:
            DD.append(R[0])
            del R[0]
        if not L:
            DD.extend(R)
            break
        elif not R:
            DD.extend(L)
            break

    return DD


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    #print I

    D = merge_sort(I)
    DD = sorted(I)
    print 'D == DD:', D == DD

    D = merge_sort(I, reverse=True)
    DD = sorted(I, reverse=True)
    print 'reverse: D == DD:', D == DD
