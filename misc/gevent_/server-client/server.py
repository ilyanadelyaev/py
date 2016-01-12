import json
import logging

import gevent.server
import gevent.pool

from gevent.monkey import patch_all; patch_all()


logger = logging.getLogger('server')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


HANDLERS_LIMIT = 10  # handle limited socket communications per time


class ServerHandler(object):
    """
    """
    class Client(object):
        def __init__(self, id_, address):
            self.id = id_
            self.address = address
            #
            self.process_counter = 5

        def __repr__(self):
            return '<Client [{}]: {}>'.format(self.id, self.address)

        def process(self, command):
            logger.info('Client: %s / Command: %s', self.id, command)
            if command == 'INIT':
                ret = 'OK'
            elif command == 'PROCESS':
                self.process_counter -= 1
                if self.process_counter <= 0:
                    ret = 'KILL'
                else:
                    ret = 'OK'
            logger.info('Client: %s / Response: %s', self.id, ret)
            return ret


    def __init__(self):
        self.clients = {}

    def __call__(self, socket, address):
        data = socket.recv(1024)
        command, client_id = json.loads(data)
        #
        client = self.clients.get(client_id, None)
        if client is None:
            client = self.clients.setdefault(client_id, self.Client(client_id, address))
        #
        ret = client.process(command)
        #
        ret = json.dumps(ret)
        socket.send(ret)
        socket.close()

if __name__ == '__main__':
    ADDRESS = '127.0.0.1'
    PORT = 4040

    try:
        gevent.server.StreamServer(
            (ADDRESS, PORT),
            ServerHandler(),
            spawn=gevent.pool.Pool(HANDLERS_LIMIT),
        ).serve_forever()
    except KeyboardInterrupt:
        pass
