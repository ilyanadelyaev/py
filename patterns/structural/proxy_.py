class Object(object):
    def do(self):
        return 'object done'


# virtual proxy

class VirtualProxy(object):
    def __init__(self):
        self.__instance = None

    def _instance(self):
        if self.__instance is None:
            self.__instance = Object()
        return self.__instance

    def do(self):
        return '{} -> {}'.format(
            'virtual proxy', self._instance().do())


# remote proxy

class RemoteProxy(object):
    def __init__(self, host):
        self.host = host

    def do(self):
        # connect to remote host
        obj = Object()
        # send data
        # recieve data
        data = obj.do()
        #
        return '{} ({}) -> {}'.format(
            'remote proxy', self.host, data)


# secure proxy

class SecureProxy(object):
    allowed_users = ('master',)

    def __init__(self, user):
        self.user = user

    def do(self):
        if self.user not in self.allowed_users:
            return
        return '{} ({}) -> {}'.format(
            'secure proxy', self.user, Object().do())


# intellectual proxy

class IntellectualProxy(object):
    def do(self):
        data = Object().do()
        data = data.upper()
        return '{} -> {}'.format(
            'intellectual proxy', data)


if __name__ == '__main__':
    vp = VirtualProxy()
    print vp.do()

    rp = RemoteProxy('localhost')
    print rp.do()

    sp = SecureProxy('master')
    print sp.do()

    ip = IntellectualProxy()
    print ip.do()
