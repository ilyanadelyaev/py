LOCK = True


class LockedException(RuntimeError):
    pass


class GlobalLock(object):
    def __init__(self, lock_name):
        self.lock_name = lock_name

    def __call__(self, func):
        def functor(*args, **kwargs):
            if LOCK:
                return func(*args, **kwargs)
            else:
                raise LockedException(self.lock_name)
        return functor

    def __enter__(self):
        if not LOCK:
            raise LockedException()

    def __exit__(self, type, value, traceback):
        pass


@GlobalLock('lock_1')
def func():
    print '! func'


if __name__ == '__main__':

    LOCK = True
    print 'try func with LOCK = True'
    func()
    print 'OK'


    LOCK = False
    print 'try func with LOCK = False'
    func()
    print 'OK'


    LOCK = True
    try:
        with GlobalLock():
            print 'under GlobalLock'
    except LockedException:
        print '! Locked'


    LOCK = False
    try:
        with GlobalLock():
            print 'under GlobalLock'
    except LockedException:
        print '! Locked'
