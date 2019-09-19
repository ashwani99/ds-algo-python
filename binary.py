from collections import deque

class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def add(self, data):
        q = deque()
        q.append(self.root)
        while q:
            popped = q.popleft()
            if 


    def max_depth(self, start=self.root):
        return self._max_depth(self, start)

    def _max_depth(self, start, depth=0):
        if start == None:
            return depth
        if not start.left and not start.right:
            return depth
        left_depth = self._max_depth(self, start.left, depth+1)
        right_depth = self._max_depth(self, start.right, depth+1)
        return max(left_depth, right_depth)
