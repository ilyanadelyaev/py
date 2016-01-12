class Stream(object):
    def __init__(self, stream=None):
        self.stream = stream

    def write(self, data):
        raise NotImplementedError


class Logger(Stream):
    def write(self, data):
        return 'log: ' + data


class ASCIIStream(Stream):
    def write(self, data):
        return 'ascii: ' + self.stream.write(data)


class ZipStream(Stream):
    def write(self, data):
        return 'ziped: ' + self.stream.write(data)


if __name__ == '__main__':
    s = ZipStream( ASCIIStream( Logger() ) )

    print s.write('hello!')
