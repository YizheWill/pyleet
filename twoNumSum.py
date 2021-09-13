
def two_num_sum(array, target):
	dict = {}
	for num in array:
		if target - num in dict:
			return [target - num, num]
		dict[num] = True
	return []

