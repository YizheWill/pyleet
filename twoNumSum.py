
def two_num_sum(array, target):
	dict = {}
	for num in array:
		if target - num in dict:
			return [target - num, num]
		dict[num] = True
	return []

if __name__ == "__main__":
	arr = [1,2,3,4,10]
	num = 11
	print(two_num_sum(arr, num))

