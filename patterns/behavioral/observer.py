class Server(object):
    def __init__(self):
        self.clients = set()

    def add_client(self, client):
        self.clients.add(client)

    def start(self):
        for c in self.clients:
            c.start()

    def execute(self):
        for c in self.clients:
            c.execute()

    def stop(self):
        for c in self.clients:
            c.stop()


class Client(object):
    def __init__(self, id_):
        self.id = id_
        self._state = 'stoped'

    def start(self):
        self._state = 'running'

    def execute(self):
        self._state = 'executing'

    def stop(self):
        self._state = 'stoped'

    def state(self):
        print self.id, self._state


if __name__ == '__main__':
    server = Server()
    clients = []

    for i in xrange(3):
        client = Client(i)
        server.add_client(client)
        clients.append(client)

    server.start()
    for c in clients:
        c.state()

    server.execute()
    for c in clients:
        c.state()

    server.stop()
    for c in clients:
        c.state()
