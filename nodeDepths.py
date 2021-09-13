def nodeDepths(root, curr_sum=0):
    # Write your code here.
    if root is None:
        return 0
    return curr_sum + nodeDepths(root.left, curr_sum + 1) + nodeDepths(root.right, curr_sum + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
