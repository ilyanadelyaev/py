MULTI_THREAD_LOGGING = True


class Logger(object):
    def __init__(self):
        if MULTI_THREAD_LOGGING:
            self.impl = MT_LoggerImpl()
        else:
            self.impl = ST_LoggerImpl()

    def log(self, data):
        raise NotImplementedError


class ConsoleLogger(Logger):
    def __init__(self):
        super(ConsoleLogger, self).__init__()

    def log(self, data):
        self.impl.console_log(data)


class FileLogger(Logger):
    def __init__(self, file_name):
        super(FileLogger, self).__init__()
        self.file_name = file_name

    def log(self, data):
        self.impl.file_log(data, self.file_name)


class RemoteLogger(Logger):
    def __init__(self, host, port):
        super(RemoteLogger, self).__init__()
        self.host, self.port = host, port

    def log(self, data):
        self.impl.remote_log(data, self.host, self.port)


class LoggerImpl(object):
    def console_log(self, data):
        raise NotImplementedError

    def file_log(self, data, file_name):
        raise NotImplementedError

    def remote_log(self, data, host, port):
        raise NotImplementedError


class ST_LoggerImpl(LoggerImpl):
    def console_log(self, data):
        print 'ST: console: {}'.format(data)

    def file_log(self, data, file_name):
        print 'ST: file ({}): {}'.format(file_name, data)

    def remote_log(self, data, host, port):
        print 'ST: remote ({}:{}): {}'.format(host, port, data)


class MT_LoggerImpl(LoggerImpl):
    def console_log(self, data):
        # lock
        print 'MT: console: {}'.format(data)

    def file_log(self, data, file_name):
        # lock
        print 'MT: file ({}): {}'.format(file_name, data)

    def remote_log(self, data, host, port):
        # lock
        print 'MT: remote ({}:{}): {}'.format(host, port, data)


if __name__ == '__main__':
    logger = RemoteLogger('localhost', 8080)
    logger.log('hello!')
