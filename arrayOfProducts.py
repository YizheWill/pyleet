# def arrayOfProducts(array):
#     # Write your code here.
# 	product = 1
# 	res = []
# 	for item in array:
# 		if item != 0:
# 			product *= item
# 	count = array.count(0)
# 	if count > 1:
# 		return [0 for _ in array]
# 	elif count == 1:
# 		for i, item in enumerate(array):
# 			if item != 0:
# 				res.append(0)
# 			else:
# 				res.append(product)
# 	else:
# 		for i, item in enumerate(array):
# 			res.append(product // item)

# 	return res
def arrayOfProducts(array):
    # Write your code here.
    left_side_array = [1 for _ in array]
    right_side_array = [1 for _ in array]
    res = [None for _ in array]
    left_running = 1
    for i in range(len(array)):
        left_side_array[i] = left_running
        left_running *= array[i]
    right_running = 1
    for j in reversed(range(len(array))):
        res[j] = left_side_array[j] * right_running
        right_running *= array[j]
    return res


if __name__ == "__main__":
    arr = [5, 1, 4, 2]
    print(arrayOfProducts(arr))
