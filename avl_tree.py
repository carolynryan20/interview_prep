class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class AvlTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def isleaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node
        new = Node(key)

        if tree is None:
            self.node = new
            self.node.left = AvlTree()
            self.node.right = AvlTree()
            print("Inserted key [{}]".format(key))
        elif key < tree.key:
            self.node.left.insert(key)
        elif key > tree.key:
            self.node.right.insert(key)
        else:
            print("Key [{}] already in tree".format(key))

        self.rebalance()

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)

        while abs(self.balance) > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.left_rotate()
                    self.update_heights()
                    self.update_balances()

                self.right_rotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.right_rotate()
                    self.update_heights()
                    self.update_balances()

                self.left_rotate()
                self.update_heights()
                self.update_balances()

    def left_rotate(self):
        new_left = self.node
        new_self = self.node.right.node
        new_right = new_self.left.node

        self.node = new_self
        new_self.left.node = new_left
        new_left.right.node = new_right

    def right_rotate(self):
        new_right = self.node
        new_self = self.node.left.node
        new_left = new_self.right.node

        self.node = new_self
        new_self.right.node = new_right
        new_right.left.node = new_left

    def update_heights(self, recurse_bool=True):
        if self.node:
            if recurse_bool:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height, self.node.right.height) + 1

        else:
            self.height = -1

    def update_balances(self, recurse_bool=True):
        if self.node:
            if recurse_bool:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def inorder_traverse(self):
        s = ""
        if self.node:
            s += self.node.left.inorder_traverse()
            s += str(self.node) + ', '
            s += self.node.right.inorder_traverse()
        return s

    def __str__(self):
        if self.node is None:
            return ''
        return '['+self.inorder_traverse()[:-2]+']'

if __name__ == "__main__":
    a = AvlTree()
    print("----- Inserting -------")
    # inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in inlist:
        a.insert(i)

    print(a)

    print("----- Deleting -------")
    a.delete(3)
    a.delete(4)
    # a.delete(5)
    print(a)

    print()
    print("Input            :", inlist)
    print("deleting ...       ", 3)
    print("deleting ...       ", 4)
    print("Inorder traversal:", a.inorder_traverse())