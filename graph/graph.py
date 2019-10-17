class Graph:
    def __init__(self):
        self._graph_dict = {}

    def add_edge(self, node1, node2):
        if node1 in self._graph_dict:
            self._graph_dict[node1].append(node2)
        else:
            self._graph_dict[node1] = [node2]
        if node2 in self._graph_dict:
            self._graph_dict[node2].append(node1)
        else:
            self._graph_dict[node2] = [node1]

    def adjacents(self, node):
        return self._graph_dict[node]
