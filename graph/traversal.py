from graph import UndirectedGraph
from collections import deque

def bfs(graph, start_node):
    visited = [start_node]
    print('Visited', start_node)
    q = deque([start_node])
    while q:
        popped_node = q.popleft()
        for node in g.adjacents(popped_node):
            if node not in visited:
                visited.append(node)
                print('Visited', node)
                q.append(node)


def dfs(graph, start_node, visited=[]):
    if start_node not in visited:
        print('Visited', start_node)
        visited.append(start_node)
    for node in graph.adjacents(start_node):
        if node not in visited:
            print('Visited', node)
            visited.append(node)
            dfs(graph, node, visited)


# DFS iterative will produce different output from recursive because of the order of insertion in the stack
def dfs_iterative(graph, start_node):
    visited = [start_node]
    stack = [start_node]
    print('Visited', start_node)
    while stack != []:
        popped = stack.pop()
        if popped not in visited:
            print('Visited', popped)
            visited.append(popped)
        for node in graph.adjacents(popped):
            if node not in visited:
                stack.append(node)


if __name__ == '__main__':
    g = UndirectedGraph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 6)
    g.add_edge(2, 7)
    g.add_edge(3, 7)

    bfs(g, 0)
    print('='*50)
    dfs(g, 0)
    print('='*50)
    dfs_iterative(g, 0)
