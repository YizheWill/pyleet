def productSum(array, depth=1):
    # Write your code here.
    res = 0
    for ele in array:
        if type(ele) is list:
            res += productSum(ele, depth + 1)
        else:
            res += ele
    return res * depth

# whileloop
# def binarySearch(array, target):
#     # Write your code here.
# 	left = 0
# 	right = len(array) - 1
# 	while left <= right:
# 		mid = (left + right) // 2
# 		if array[mid] == target:
# 			return mid
# 		elif target < array[mid]:
# 			right = mid - 1
# 		else:
# 			left = mid + 1
# 	return -1
