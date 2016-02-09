import ma


class B(ma.First, ma.Second):
    def __init__(self, i):
        super(B, self).__init__(i)
        #
        self.first_value = 0
        self.second_value = 1
