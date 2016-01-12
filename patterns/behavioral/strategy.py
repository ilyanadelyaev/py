class Compression(object):
    pass


class ZIP_Compression(Compression):
    def __init__(self, level):
        self.level = level

    def compress(self, data):
        print 'ZIP compress "{}" with level {}'.format(data, self.level)


class ARJ_Compression(Compression):
    def __init__(self, level):
        self.level = level

    def compress(self, data):
        print 'ARJ compress "{}" with level {}'.format(data, self.level)


class Compressor(object):
    def __init__(self, compression):
        self.compression = compression

    def compress(self, data):
        return self.compression.compress(data)


if __name__ == '__main__':
    c = Compressor(
        ZIP_Compression(7)
    )

    c.compress('aabb')
