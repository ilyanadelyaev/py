import collections


matrix = [
[ 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, ],
[ 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, ],
[ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, ],
[ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
[ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
]


class Graph(object):
    class _Node(object):
        def __init__(self, _id):
            self._id = _id
            self.links = []

        def __repr__(self):
            return 'Node {} : {}'.format(self._id, str(self.links))

    def __init__(self):
        self._nodes = {}

    def __repr__(self):
        res = []
        for n in self._nodes.itervalues():
            res.append(str(n))
        return '\n'.join(res)

    def read(self, matrix):
        self._nodes[0] = self._Node(0)

        for i_row, row in enumerate(matrix):
            for i_c, c in enumerate(row):
                if i_c > i_row:
                    break
                if c:
                    self._nodes[i_row] = self._Node(i_row)
                    self._nodes[i_row].links.append(i_c)
                    self._nodes[i_c].links.append(i_row)

    def breadth_first_search(self, start, end):
        start_node = self._nodes.get(start, None)
        end_node = self._nodes.get(end, None)
        if not start_node or not end_node:
            return

        line = collections.deque((start_node,))
        processed_nodes_ids = set([start_node._id])
        path = {}

        while line:
            node = line.pop()
            for child_node_id in node.links:
                # check if processed
                if child_node_id in processed_nodes_ids:
                    continue
                processed_nodes_ids.add(child_node_id)
                # add to line
                child_node = self._nodes[child_node_id]
                line.appendleft(child_node)
                # memo path
                path[child_node_id] = node._id

        return path



if __name__ == '__main__':

    g = Graph()

    g.read(matrix)

    print g

    print '0 -> 10', g.breadth_first_search(0, 10)
