class Executor(object):
    def step_one(self):
        print 'base one'

    def step_two(self):
        print 'base two'

    def execute(self):
        self.step_one()
        self.step_two()


class MyExecutor(Executor):
    def step_two(self):
        print 'my two'


if __name__ == '__main__':
    e = MyExecutor()
    e.execute()
