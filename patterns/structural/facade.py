class Processor(object):
    states = {}

    def __init__(self):
        self._state = 0

    def start(self):
        raise NotImplementedError

    def state(self):
        return self.states.get(self._state, 'invalid')

    def process(self):
        if self._state > 0:
            self._state -= 1


class ShopCart(Processor):
    states = {
        2: 'item in bag',
        1: 'send request to warehouse',
        0: 'bag processed',
    }

    def start(self):
        self._state = 2


class Warehouse(Processor):
    states = {
        3: 'void',
        2: 'request recieved',
        1: 'send request to shipping department',
        0: 'warehouse processed',
    }

    def start(self):
        self._state = 3


class Shipping(Processor):
    states = {
        5: 'void',
        4: 'void',
        3: 'request recieved',
        2: 'packing product',
        1: 'has shiped by airplane',
        0: 'shipping processed',
    }

    def start(self):
        self._state = 5


class StoreFacade(object):
    def __init__(self):
        self.shopcart = ShopCart()
        self.warehouse = Warehouse()
        self.shipping = Shipping()

    def order_product(self, product):
        print 'Order: {}'.format(product)
        self.shopcart.start()
        self.warehouse.start()
        self.shipping.start()

    def process(self):
        self.shopcart.process()
        self.warehouse.process()
        self.shipping.process()

    def state(self):
        return '{} : {} : {}'.format(
            self.shopcart.state(),
            self.warehouse.state(),
            self.shipping.state(),
        )


if __name__ == '__main__':
    f = StoreFacade()

    f.order_product('notebook')

    for _ in xrange(5):
        print f.state()
        f.process()
    print f.state()
