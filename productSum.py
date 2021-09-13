def productSum(array, depth=1):
    # Write your code here.
    res = 0
    for ele in array:
        if type(ele) is list:
            res += productSum(ele, depth + 1)
        else:
            res += ele
    return res * depth
