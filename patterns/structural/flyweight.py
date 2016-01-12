class Pixel(object):
    def draw(self, pos):
        print '{} / {} / {}'.format(
            self.color,
            self.size,
            pos,
        )


class RedPixel(Pixel):
    def __init__(self):
        self.color = 'red'
        self.size = 2


class GreenPixel(Pixel):
    def __init__(self):
        self.color = 'green'
        self.size = 4


class BluePixel(Pixel):
    def __init__(self):
        self.color = 'blue'
        self.size = 2


class PixelFactory(object):
    def draw(self, image):
        sequence = []
        for p in image:
            if p == 'r':
                sequence.append(RedPixel())
            elif p == 'g':
                sequence.append(GreenPixel())
            elif p == 'b':
                sequence.append(BluePixel())
        for i, p in enumerate(sequence):
            p.draw(i)


if __name__ == '__main__':
    f = PixelFactory()

    f.draw('rgbrgb')
