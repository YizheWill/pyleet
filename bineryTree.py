class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self is None:
            self = BST(value)
        elif self.left is None and value < self.value:
            self.left = BST(value)
        elif self.right is None and value >= self.value:
            self.right = BST(value)
        elif value < self.left:
            self.left.insert(value)
        elif value >= self.right:
            self.right.insert(value)
        return self

    def search(self, value, parent=None, direction=''):
        if self is None:
            return False
        else:
            if value < self.value:
                return self.left.contain(value, self, 'left')
            elif value > self.value:
                return self.right.contain(value, self, 'right')
            else:
                return [True, self, parent, direction]

    def contain(self, value):
        res = self.search(value, None, '')
        if res is False:
            return False
        else:
            return True

    def remove(self, value):

        if self is None:
            return self
        elif value < self.value:
            self.left.remove(value)
        elif value > self.value:
            self.right.remove(value)
        else:
            if self.left is None and self.right is None:
                self = None
            elif self.left is None:
                self = self.right
            elif self.right is None:
                self = self.left
            else:
                val = self.right.get_min_value()
                self.value = val
                self.right.remove(val)
        return self

    def get_min_value(self):
        if self is None:
            return None
        curr = self
        while self.left:
            curr = self
            self = self.left
        return self.value
