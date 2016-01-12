class Machine(object):
    def __init__(self):
        self._state = 'stopped'

    def start(self):
        self._state = 'STARTED'

    def stop(self):
        self._state = 'stopped'

    def state(self):
        return self._state


class Command(object):
    def execute(self):
        raise NotImplementedError


class Command_Start(Command):
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        self.machine.start()


class Command_Stop(Command):
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        self.machine.stop()


if __name__ == '__main__':
    m = Machine()
    print m.state()

    commands = [
        Command_Start(m),
        Command_Stop(m),
    ]

    for c in commands:
        c.execute()
        print m.state()
