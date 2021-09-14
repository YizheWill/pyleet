def firstDuplicateValue(array):
    # Write your code here.
    hash = {}
    for item in array:
        if hash.get(item):
            return item
        hash[item] = True
    return -1


def firstDuplicateValue(array):
    for num in array:
        absNum = abs(num)
        if array[absNum - 1] < 0:
            return absNum
        array[absNum - 1] *= -1
    return -1
