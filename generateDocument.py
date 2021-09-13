def generateDocument(characters, document):
    # Write your code here.
    hash = {}
    for item in characters:
        hash[item] = hash[item] + 1 if hash.get(item) is not None else 1
    for char in document:
        if hash.get(char) is None or hash[char] == 0:
            return False
        else:
            hash[char] -= 1
    return True
