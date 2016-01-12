import uuid

import gevent
import gevent.queue
import geventwebsocket.handler
import geventwebsocket.exceptions

from gevent.monkey import patch_all; patch_all()


class WebRender(object):
    """
    Render templates from cache
    """

    TEMPLATES = {
        '/': './templates/index.html'
    }

    CACHE_ACTIVE = True
    CACHE = {}

    @classmethod
    def process(cls, env, start_response):
        path = env['PATH_INFO']
        if path in cls.TEMPLATES:
            start_response('200 OK', [('Content-Type', 'text/html')])

            template = cls.TEMPLATES[path]
            template_body = cls.CACHE.get(template, None) if cls.CACHE_ACTIVE else None
            if template_body is None:
                with open('./templates/index.html', 'r') as f:
                    template_body = f.read()
                    if cls.CACHE_ACTIVE:
                        cls.CACHE[template] = template_body
            return [template_body]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return ['<h1>Not Found</h1>']


# Messenger

class Messenger(object):
    """
    Implement send and recieve handlers
    Process broadcasting
    """

    queues = {}  # for all opened web-sockets

    class RecieverProcessor(object):
        """
        recieve messages from web sockets and add it to queue
        """
        def __call__(self, env, _):
            ws = env['wsgi.websocket']
            while True:
                data = ws.receive()
                if data is None:
                    break
                for queue in Messenger.queues.itervalues():
                    queue.put(data)
            ws.close()

    class SenderProcessor(object):
        """
        send messages to web-sockets from queue
        """
        def __call__(self, env, _):
            ws = env['wsgi.websocket']
            _id = uuid.uuid4()
            Messenger.queues[_id] = gevent.queue.Queue()
            try:
                for data in Messenger.queues[_id]:
                    try:
                        ws.send(data)
                    except geventwebsocket.exceptions.WebSocketError:  # disconnected
                        break
            finally:
                del Messenger.queues[_id]


if __name__ == '__main__':
    #
    ADDRESS = '127.0.0.1'
    WEB_PORT = 8000
    REVIEVER_PORT = 4030
    SENDER_PORT = 4031

    # HTTP render
    web_render = gevent.pywsgi.WSGIServer(
        (ADDRESS, WEB_PORT),
        WebRender.process
    )

    # Messenger
    reciever = gevent.pywsgi.WSGIServer(
        (ADDRESS, REVIEVER_PORT),
        Messenger.RecieverProcessor(),
        handler_class=geventwebsocket.handler.WebSocketHandler
    )
    sender = gevent.pywsgi.WSGIServer(
        (ADDRESS, SENDER_PORT),
        Messenger.SenderProcessor(),
        handler_class=geventwebsocket.handler.WebSocketHandler
    )

    print 'Go: http://{}:{}/'.format(ADDRESS, WEB_PORT)

    # run
    web_render.start()
    reciever.start()
    sender.start()
    try:
        gevent.joinall([
            web_render._stop_event,
            reciever._stop_event,
            sender._stop_event,
        ])
    except KeyboardInterrupt:
        pass
