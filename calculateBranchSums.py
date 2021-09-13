class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    arr = []
    helper(root, 0, arr)
    return arr


def helper(root, curr_sum, res_arr):
    if root is None:
        return
    curr_sum += root.value
    if root.left is None and root.right is None:
        res_arr.append(curr_sum)
        return
    helper(root.left, curr_sum, res_arr)
    helper(root.right, curr_sum, res_arr)
