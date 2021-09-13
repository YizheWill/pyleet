def moveElementToEnd(array, toMove):
    # Write your code here.
	count = array.count(toMove)
	array = list(filter(lambda val: val != toMove, array))
	array.extend([toMove for x in range(count)])
	return array
