def isValidSubsequence(array, sequence):
    # Write your code here.
	i, j = 0, 0
	while i < len(array):
		if array[i] == sequence[j]:
			j+=1
			if j>= len(sequence):
				return True
		i+= 1
	return False
		
