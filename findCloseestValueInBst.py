def findClosestValueInBst(tree, target):
    # Write your code here.
    return helper(tree, target, tree.value)


def helper(node, target, closest):
    currVal = node.value
    if abs(target - currVal) < abs(target - closest):
        closest = currVal
    if target < node.value and node.left is not None:
        return helper(node.left, target, closest)
    elif target > node.value and node.right is not None:
        return helper(node.right, target, closest)
    return closest
