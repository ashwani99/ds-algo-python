from collections import deque

class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def add(self, data):
        newnode = Node(data)
        q = deque()
        q.append(self.root)
        while q:
            popped = q.popleft()
            if popped.left:
                q.append(popped.left)
            else:
                popped.left = newnode
                return
            if popped.right:
                q.append(popped.right)
            else:
                popped.right = newnode
                return

    def max_depth(self, root):
        return self._max_depth(root)

    def _max_depth(self, start):
        if start == None:
            return 0
        left_depth = self._max_depth(start.left)
        right_depth = self._max_depth(start.right)
        return 1 + max(left_depth, right_depth)

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(root.data, end=' ')
            self.print_inorder(root.right)

    def diameter(self, root):
        if root:
            left_height = self.max_depth(root.left)
            right_height = self.max_depth(root.right)

            left_diameter = self.diameter(root.left)
            right_diameter = self.diameter(root.right)

            return max(1+left_height+right_height, left_diameter, right_diameter)
        return 0


if __name__ == '__main__':
    bt = BinaryTree(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    bt.add(0)
    print('Printing inorder...')
    bt.print_inorder(bt.root)
    print()
    print('Max depth of the tree:', bt.max_depth(bt.root))

    print('Diameter of the tree is:', bt.diameter(bt.root))
