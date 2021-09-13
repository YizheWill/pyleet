class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        if self is None:
            return
        array.append(self.name)
        for item in self.children:
            item.depthFirstSearch(array)

        return array
