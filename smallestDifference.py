def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	i, j = 0, 0
	arrayOne.sort()
	arrayTwo.sort()
	min_diff = abs(arrayOne[0] - arrayTwo[0])
	res = [arrayOne[0], arrayTwo[0]]
	while i < len(arrayOne) and j < len(arrayTwo):
		first, second = arrayOne[i], arrayTwo[j]
		curr_diff = abs(first - second)
		if curr_diff <= min_diff:
			res = [first, second]
			min_diff = curr_diff
		if first > second:
			j += 1
		else:
			i += 1
	return res
