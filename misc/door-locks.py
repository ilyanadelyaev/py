locks = {}

for i in xrange(1, 100+1):
    for j in xrange(i, 100+1, i):
        locks.setdefault(j, 0)
        locks[j] += 1

for l in locks:
    if locks[l] % 2 == 1:
        print l, locks[l]
