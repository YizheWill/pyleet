def binarySearch(array, target):
    # Write your code here.
	if len(array) == 0:
		return -1
	mid_idx = len(array) // 2
	left = array[:mid_idx]
	right = array[mid_idx + 1:]
	if target == array[mid_idx]:
		return mid_idx
	elif target < array[mid_idx]:
		return binarySearch(left, target)
	else:
		rightIdx = binarySearch(right, target)
		return rightIdx + mid_idx + 1 if rightIdx >= 0 else -1
