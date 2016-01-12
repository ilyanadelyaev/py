data = [1, 2, 3]

def iter_loop(d):
    pos = 0
    length = len(d)
    while True:
        r = yield d[pos]
        if r:
            return
        pos += 1
        if pos >= length:
            pos = 0


i = iter_loop(data)

print i.next()
print i.next()
print i.next()
print i.next()
print i.next()
try:
    print i.send(1)
except StopIteration:
    print 'done'
