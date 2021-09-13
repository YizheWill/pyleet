def isPalindrome(string):
    # Write your code here.
	length = len(string)
	for i in range(len(string) // 2):
		if string[i] != string[length - i - 1]:
			return False
	return True
