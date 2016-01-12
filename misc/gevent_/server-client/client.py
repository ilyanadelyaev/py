import os
import uuid
import json
import time
import socket
import logging


logger = logging.getLogger('client')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


CLIENTS_COUNT = 100


ADDRESS = '127.0.0.1'
PORT = 4040

SEND_TIMEOUT = 2.0
RECIEVE_TIMEOUT = 2.0


def client_executor():
    # ID
    client_id = str(uuid.uuid4())

    # init client on server
    status = communicate(('INIT', client_id))
    if status != 'OK':
        return -1

    # make some work
    while True:
        time.sleep(1.0)
        #
        data = communicate(('PROCESS', client_id))
        if data == 'OK':
            continue
        elif data == 'KILL':
            break

    return 0


def communicate(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDRESS, PORT))
    sock.settimeout(SEND_TIMEOUT)
    logger.info('Send: %s', data)
    sock.send(json.dumps(data))
    data = json.loads(sock.recv(1024))
    sock.close()
    logger.info('Response: %s', data)
    return data


if __name__ == '__main__':
    # start clients
    client_pids = []
    for i in xrange(CLIENTS_COUNT):
        pid = os.fork()
        if pid == 0:
            os._exit(client_executor())
        else:
            logger.info('Client [%d] started', pid)
            client_pids.append(pid)
    # wait clients
    while client_pids:
        pid, st = os.wait()
        client_pids.remove(pid)
        logger.info('Client [%s] finished with "%s"', pid, st)
