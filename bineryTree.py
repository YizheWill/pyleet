class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.left is None and self.right is None:
            self = BST(value)
        elif self.left is None and value < self.value:
            self.left = BST(value)
        elif self.right is None and value >= self.value:
            self.right = BST(value)
        elif value < self.left:
            self.left.insert(value)
        elif value >= self.left:
            self.right.insert(value)
        return self
