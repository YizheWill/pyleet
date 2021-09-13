def firstNonRepeatingCharacter(string):
    # Write your code here.
    hash = {}
    for char in string:
        hash[char] = hash[char] + 1 if hash.get(char) else 1
    for idx, char in enumerate(string):
        if hash.get(char) == 1:
            return idx
    return -1
