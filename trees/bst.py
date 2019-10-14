from binary import Node

class BST:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        ptr = self.root
        while ptr:
            if data < ptr.data:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = Node(data)
                    return
            else:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = Node(data)
                    return

    def insert_recusive(self, root, data):
        raise NotImplementedError

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)


if __name__ == '__main__':
    bst = BST(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.inorder(bst.root)
