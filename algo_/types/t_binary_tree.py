class BinaryTree(object):
    class _Node(object):
        def __init__(self, key, value, parent):
            self.key = key
            self.value = value
            #
            self.parent = parent
            self.left = None
            self.right = None

        def __str__(self):
            return self.value

        def __repr__(self):
            return '{} {} {}'.format('/' if self.left else '.', self.key, '\\' if self.right else '.')

    def __init__(self):
        self.head = None

    def __get_node_by_key(self, key):
        node = self.head
        while True:
            if node is None:
                raise KeyError
            elif key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right

    def __contains__(self, key):
        try:
            self.__get_node_by_key(key)
            return True
        except KeyError:
            return False

    def __setitem__(self, key, value):
        if self.head is None:
            self.head = BinaryTree._Node(key, value, None)
            return
        current = self.head
        while True:
            if key == current.key:
                current.value = value
                return
            elif key < current.key:
                if current.left is None:
                    current.left = BinaryTree._Node(key, value, current)
                    return
                else:
                    current = current.left
                    pass
            else:
                if current.right is None:
                    current.right = BinaryTree._Node(key, value, current)
                    return
                else:
                    current = current.right

    def __getitem__(self, key):
        return self.__get_node_by_key(key).value

    def __delitem__(self, key):
        def _set_new_parent_node(node, val):
            parent = node.parent
            if parent is None:  # head node
                self.head = val
            elif parent.left == node:
                parent.left = val
            elif parent.right == node:
                parent.right = val
            else:
                return
            if val:
                val.parent = parent

        node = self.__get_node_by_key(key)
        if node.left is None and node.right is None:  # no nodes
            _set_new_parent_node(node, None)
        elif node.right is None:  # left only
            _set_new_parent_node(node, node.left)
        elif node.left is None:  # right only
            _set_new_parent_node(node, node.right)
        else:  # two nodes
            cutted_node = node.left
            _set_new_parent_node(node, node.right)
            # find min
            _min = node.right
            while True:
                if _min.left is None:
                    break
                _min = _min.left
            _min.left = cutted_node
            cutted_node.parent = _min

    @classmethod
    def __sorted_list_for_node(cls, node, reverse=False):
        if node is None:
            return []
        l = cls.__sorted_list_for_node(node.left, reverse=reverse)
        r = cls.__sorted_list_for_node(node.right, reverse=reverse)
        n = [(node.key, node.value)]
        if reverse:
            return r + n + l
        else:
            return l + n + r

    def sorted(self, reverse=False):
        return self.__sorted_list_for_node(self.head, reverse=reverse)

    def __check_ballance(self):
        pass

    def ballance(self):
        if __check_ballance():
            return
        pass

    def draw(self):
        output = {}
        level = 0
        to_check = [self.head]
        while True:
            _to_check = to_check[:]
            to_check = []
            for o in _to_check:
                output.setdefault(level, []).append(o)
                to_check.extend([j for j in [o.left, o.right] if j])
            if not to_check:
                break
            level += 1
        for l in sorted(output):
            print output[l]


if __name__ == '__main__':
    # add / remove / get

    bt = BinaryTree()

    bt[10] = 100

    assert 10 in bt
    assert bt[10] == 100
    assert -1 not in bt

    del bt[10]
    try:
        del bt[-1]
        assert False
    except KeyError:
        assert True

    assert 10 not in bt
    assert bt.head is None

    # remove from tails and head

    I = [(22, 220), (39, 390), (50, 500), (56, 560),
        (4, 40), (44, 440), (31, 310), (28, 280),
        (32, 320), (55, 550), (45, 450)]

    bt = BinaryTree()
    for k, v in I:
        bt[k] = v

    del bt[55]
    assert 55 not in bt
    del bt[56]
    assert 56 not in bt
    del bt[45]
    assert 45 not in bt
    del bt[22]
    assert 22 not in bt

    #bt.draw()

    # check for correct structure after delete

    D = bt.sorted()
    assert D == sorted(D, key=lambda x: x[0])

    # random

    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    I = [(i, i*10) for i in I]

    bt = BinaryTree()
    for k, v in I:
        bt[k] = v

    D = bt.sorted()
    DD = sorted(I, key=lambda x: x[0])
    assert D == DD

    D = bt.sorted(reverse=True)
    DD = sorted(I, key=lambda x: x[0], reverse=True)
    assert D == DD

    for k, v in D:
        # in
        assert k in bt
        assert bt[k] == v
        #
        del bt[k]
        # out
        assert k not in bt
        try:
            bt[k]
            assert False
        except KeyError:
            assert True
        # check structure
        D = bt.sorted()
        assert D == sorted(D, key=lambda x: x[0])
