def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    res = []
    for idx, item in enumerate(array):
        i, j = idx + 1, len(array) - 1
        while i < j:
            three_sum = item + array[i] + array[j]
            if three_sum == targetSum:
                res.append([item, array[i], array[j]])
                i += 1
                j -= 1
            elif targetSum < three_sum:
                j -= 1
            else:
                i += 1

    return res
