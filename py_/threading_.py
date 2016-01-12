import time
import threading


print_lock = threading.Lock()

def log(*args):
    with print_lock:
        for a in args:
            print a,
        print

# mutex

var = 0
lock = threading.Lock()

def f(r):
    global var
    for i in xrange(r):
        # inc and log at same time
        with lock:
            var += 1
            log(var)

th = [
    threading.Thread(target=f, args=(2,)),
    threading.Thread(target=f, args=(2,)),
]
[t.start() for t in th]
[t.join() for t in th]

print '=' * 10


# semahpore

N = 2
semaphore = threading.BoundedSemaphore(N)

def f(id_):
    # N threads simultaneously
    semaphore.acquire()
    for i in xrange(4):
        log(id_, i)
        time.sleep(0.1)
    semaphore.release()

th = [threading.Thread(target=f, args=(i,)) for i in xrange(5)]
[t.start() for t in th]
[t.join() for t in th]

print '=' * 10


# event

var = 0
event = threading.Event()

def watcher():
    global var
    for i in xrange(4):
        event.wait()
        log(var)
        event.clear()

def modifier():
    global var
    for i in xrange(4):
        var += 1
        # notify about update
        event.set()
        time.sleep(0.1)

th = [
    threading.Thread(target=modifier),
    threading.Thread(target=watcher),
]
[t.start() for t in th]
[t.join() for t in th]

print '=' * 10


# r-lock

val = 0
rlock = threading.RLock()

def f_1():
    global val
    rlock.acquire()
    val += 1
    f_2()
    rlock.release()

def f_2():
    global val
    rlock.acquire()
    val += 1
    rlock.release()

f_1()
print val
