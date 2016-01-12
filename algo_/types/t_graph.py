import collections


class Graph(object):
    class Node(object):
        class Edge(object):
            def __init__(self, node_to, weight):
                self.node_to = node_to
                self.weight = weight

            def __repr__(self):
                return '<Edge to {} [{}]>'.format(
                    self.node_to,
                    self.weight
                )

        def __init__(self, _id):
            self.id = _id
            self.connections_ids = set()  # for non-weighted graph
            self.edges = set()  # for weighted graph

        def __repr__(self):
            return '<Node: [{}] -> {}>'.format(
                self.id,
                self.edges if self.edges else self.connections_ids,
            )

    def __init__(self):
        self.nodes = {}

    # path search

    def breadth_first_search(self, start, end):
        # reverse start and end to correctly return path in end
        start, end = end, start
        # check params
        if start == end:
            return None
        start_node = self.nodes.get(start, None)
        end_node = self.nodes.get(end, None)
        if start_node is None or end_node is None:
            return None
        #
        queue = collections.deque((start_node,))
        processed_node_ids = set()
        prev_node_ids = {}
        # search for end_node
        while queue:
            node = queue.pop()
            if end_node.id in node.connections_ids:
                prev_node_ids[end_node.id] = node.id
                break
            processed_node_ids.add(node.id)
            for current_node_id in node.connections_ids:
                if current_node_id in processed_node_ids:
                    continue
                prev_node_ids[current_node_id] = node.id
                if current_node_id not in processed_node_ids:
                    queue.appendleft(self.nodes[current_node_id])
        if end_node.id not in prev_node_ids:
            return None
        # collect path
        path = [end_node.id]
        prev_node_id = end_node.id
        while True:
            prev_node_id = prev_node_ids.get(prev_node_id, None)
            if prev_node_id is None:
                break
            path.append(prev_node_id)
        return path

    def depth_first_search(self, start, end):
        # reverse start and end to correctly return path in end
        start, end = end, start
        # check params
        if start == end:
            return None
        start_node = self.nodes.get(start, None)
        end_node = self.nodes.get(end, None)
        if start_node is None or end_node is None:
            return None
        #
        queue = collections.deque((start_node,))
        processed_node_ids = set()
        prev_node_ids = {}
        # search for end_node
        while queue:
            node = queue.pop()
            if end_node.id in node.connections_ids:
                prev_node_ids[end_node.id] = node.id
                break
            processed_node_ids.add(node.id)
            for current_node_id in node.connections_ids:
                if current_node_id in processed_node_ids:
                    continue
                prev_node_ids[current_node_id] = node.id
                if current_node_id not in processed_node_ids:
                    queue.append(self.nodes[current_node_id])
        if end_node.id not in prev_node_ids:
            return None
        # collect path
        path = [end_node.id]
        prev_node_id = end_node.id
        while True:
            prev_node_id = prev_node_ids.get(prev_node_id, None)
            if prev_node_id is None:
                break
            path.append(prev_node_id)
        return path

    def dijkstra(self, start, end):
        pass

    # create graph

    @classmethod
    def graph_from_adjacency_matrix(cls, vertices_count, matrix):
        nodes = {}
        for i in xrange(vertices_count):
            node = cls.Node(i)
            for j in xrange(vertices_count):
                if not matrix[i][j]:
                    continue
                node.connections_ids.add(j)
            nodes[node.id] = node
        return nodes

    @classmethod
    def weighted_graph_from_adjacency_matrix(cls, vertices_count, matrix):
        nodes = {}
        for i in xrange(vertices_count):
            node = cls.Node(i)
            for j in xrange(vertices_count):
                if matrix[i][j] is None:
                    continue
                weight = matrix[i][j]
                edge = cls.Node.Edge(j, weight)
                node.edges.add(edge)
            nodes[node.id] = node
        return nodes

    # adjacency matrix

    @staticmethod
    def read_adjacency_matrix(file_name):
        with open(file_name) as f:
            vertices_count = int(f.readline().strip())
            adjacency_matrix = []
            i = 0
            for line in f:
                line = line.strip()
                if not line:
                    continue
                row = []
                for el in line:
                    try:
                        el = int(el.strip())
                    except ValueError:
                        continue
                    row.append(el)
                adjacency_matrix.append(row)
        return vertices_count, adjacency_matrix

    # conversions

    @staticmethod
    def convert_adjacency_matrix_to_edges(vertices_count, matrix, directed=False):
        edges = []
        for i in xrange(vertices_count):
            for j in xrange(vertices_count):
                if matrix[i][j]:
                    if directed:
                        edges.append((i, j))
                    else:
                        if i > j:
                            continue
                        edges.append((i, j))
        return edges

    @staticmethod
    def convert_adjacency_matrix_to_adjacency_list(vertices_count, matrix):
        return [[j for j, el in enumerate(row) if el] for row in matrix]


if __name__ == '__main__':

    # WEIGHTED GRAPH

    print '# WEIGHTED GRAPH'

    # search

    print '# search'

    # http://graphonline.ru/?graph=BzdcZJnByXeGozze

    vertices_count = 4
    adjacency_matrix = [
        [None, 0, None, 0],
        [0, None, 1, None],
        [None, 1, None, 0],
        [0, None, 0, None],
    ]

    wg = Graph()
    wg.nodes = Graph.weighted_graph_from_adjacency_matrix(
        vertices_count, adjacency_matrix)

    # Dijkstra

    path = wg.dijkstra(0, 2)
    print 'Dijkstra: 0 -> 2', path

    # NON WEIGHTED GRAPH

    print '# NON WEIGHTED GRAPH'

    # search

    print '# search'

    # matrix from http://graphonline.ru/?graph=rZkApMMhIYTUgEEJ

    vertices_count, adjacency_matrix = Graph.read_adjacency_matrix('./types/t_graph.matrix')

    g = Graph()
    g.nodes = Graph.graph_from_adjacency_matrix(
        vertices_count, adjacency_matrix)

    # BFS

    path = g.breadth_first_search(18, 12)
    print 'BFS: 18 -> 12:', path
    path = g.breadth_first_search(6, 13)
    print 'BFS: 6 -> 13:', path

    # DFS

    path = g.depth_first_search(18, 12)
    print 'GFS: 18 -> 12:', path
    path = g.depth_first_search(6, 13)
    print 'GFS: 6 -> 13:', path

    # misc

    print '# misc'

    # conversions

    vertices_count = 5
    adjacency_matrix = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    # edges list

    edges_list = Graph.convert_adjacency_matrix_to_edges(
        vertices_count, adjacency_matrix)
    print 'edges_list:', edges_list

    # directed edges list

    directed_edges_list = Graph.convert_adjacency_matrix_to_edges(
        vertices_count, adjacency_matrix, directed=True)
    print 'directed_edges_list:', directed_edges_list

    # vertices

    vertices_list = Graph.convert_adjacency_matrix_to_adjacency_list(
        vertices_count, adjacency_matrix)
    print 'vertices_list:', vertices_list
