def findThreeLargestNumbers(array):
    # Write your code here.
    if len(array) < 3:
        return []
    res = array[:3]
    res = sort_array(res)
    for item in array[3:]:
        add_num(res, item)
        print(res)
    return res


def add_num(array, item):
    if item < array[0]:
        return
    elif item >= array[2]:
        array[0], array[1], array[2] = array[1], array[2], item
    elif item >= array[1]:
        array[0], array[1], array[2] = array[1], item, array[2]
    else:
        array[0], array[1], array[2] = item, array[1], array[2]


def sort_array(array):
    a, b, c = array
    if min(a, b, c) == a:
        return[a, min(b, c), max(b, c)]
    elif min(a, b, c) == b:
        return[b, min(a, c), max(a, c)]
    elif min(a, b, c) == c:
        return[c, min(a, b), max(a, b)]


if __name__ == '__main__':
    arr = [55, 7, 8, 3, 43, 11]
    # print(sort_array(arr))
    print(findThreeLargestNumbers(arr))
