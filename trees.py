class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def main():
    t1 = Tree(1)
    t2 = Tree(2)
    t3 = Tree(3,t1,t2)
    print(t3)

main()