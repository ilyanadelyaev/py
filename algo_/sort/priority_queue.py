class PriorityQueue(object):
    def __init__(self):
        self.__queue = []

    def push(self, key):
        self.__queue.append(key)

    def pop(self):
        mi = 0
        mv = None
        for i, v in enumerate(self.__queue):
            if v > mv:
                mv = v
                mi = i
        return self.__queue.pop(mi)

    def __len__(self):
        return len(self.__queue)


if __name__ == '__main__':
    pq = PriorityQueue()

    pq.push(1)
    pq.push(5)
    pq.push(9)
    pq.push(4)
    pq.push(0)

    assert len(pq) == 5

    assert pq.pop() == 9
    assert pq.pop() == 5
    assert pq.pop() == 4
    assert pq.pop() == 1
    assert pq.pop() == 0

    assert len(pq) == 0
