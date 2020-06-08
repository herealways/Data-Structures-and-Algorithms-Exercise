#      9
#    4   20
#  1 6 15 170
from collections import deque


class Node():
    def __init__(self, value: int):
        self.left = None
        self.right = None
        self.value = value

    # def insert(self, value):
    #     if value < self.value:  # Left
    #         if self.left is None:  # Find where to insert
    #             self.left = Node(value)
    #         else:  # There is child node, we need to do more compare
    #             self.left.insert(value)
    #     elif value > self.value:  # Right
    #         if self.right is None:
    #             self.right = Node(value)
    #         else:
    #             self.right.insert(value)
    #     else:
    #         raise Exception('No duplicate node allowed')

    def __str__(self):
        return str(self.__dict__)

    __repr__ = __str__


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value: int = None):
        # if self.root is None:
        #     self.root = Node(value)
        # else:
        #     self.root.insert(value)
        if self.root is None:
            self.root = Node(value)
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    return
                else:
                    current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = Node(value)
                    return
                else:
                    current_node = current_node.right
            else:
                raise Exception('No duplicate node allowed')

    def search(self, value):
        current_node = self.root
        if current_node is None:
            return False
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return current_node
        return False

    def remove(self, value):
        # https://visualgo.net/bn/bst
        # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
        # Firstly we need to search for value
        # If value is leaf node: remove directly
        # elif value has one child: Use child to replace value
        # elif value has two children:  (complicated, do some demo on visualgo)
        #   replace value with successor:
        # 1. Find the right node of the children v2
        # 2. If v2 has no child, replace value with v2
        #   else: find v2's minimum child(successor),
        #         and replace value with minimum child
        #         two more situations here:
        #         successor is a leaf node or not

        # target_node = self.search(value, True)
        # Find target_node (the node to be deleted) and target's parent
        current_node = self.root
        if current_node is None:
            return False
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                # Indicate which child of the parent is the target_node
                direction = 'left'
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                direction = 'right'
                current_node = current_node.right
            else:
                target_node = current_node
                break
        else:
            return False  # Cannot find the node to remove
        # When target_node is leaf node:
        if target_node.left is None and target_node.right is None:
            exec(f'parent_node.{direction} = None')
            return

        # When target_node has one child:
        if target_node.left is None and target_node.right is not None:
            child_node = target_node.right
            target_node.value = child_node.value
            target_node.left = child_node.left
            target_node.right = child_node.right
            return

        if target_node.left is not None and target_node.right is None:
            child_node = target_node.left
            target_node.value = child_node.value
            target_node.left = child_node.left
            target_node.right = child_node.right
            return

        # When target_node has two child:
        # Get target_node's right child
        target_right_node = target_node.right
        if target_right_node.left is None and target_right_node.right is None:
            target_node.value = target_right_node.value
            target_node.right = None
            return
        # Find successor which is the minimum value on target_right_node
        successor = target_right_node
        while True:
            if successor.left is not None:
                successor_parent = successor
                successor = target_right_node.left
            else:
                break
        # Start to replace value with successor
        target_node.value = successor.value
        # If successor is a leaf node
        if successor.left is None and successor.right is None:
            successor_parent.left = None
        else:
            target_node.right = successor.right

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value, end=' ')
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.preorder(node.left)
        self.preorder(node.right)
        print(node.value, end=' ')

    def levelorder(self):
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            node = q.popleft()
            print(node.value, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


if __name__ == "__main__":
    MyBST = BinarySearchTree()
    MyBST.insert(9)
    MyBST.insert(4)
    MyBST.insert(6)
    MyBST.insert(20)
    MyBST.insert(170)
    MyBST.insert(300)
    MyBST.insert(15)
    MyBST.insert(1)
    print(MyBST.root)
    print(MyBST.search(20))
    MyBST.remove(170)
    print(MyBST.root)
    MyBST.inorder(MyBST.root)
    print()
    MyBST.preorder(MyBST.root)
    print()
    MyBST.levelorder()
