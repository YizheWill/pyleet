def sortedSquaredArray(array):

    # i = 0
    # j = len(array) - 1
    # res = []
    # while i <= j:
    #     if abs(array[j]) > abs(array[i]):
    #         res = array[j] * array[j] + res
    #         j -= 1
    #     else:
    #         res = array[i] * array[i] + res
    #         i += 1
    # return res
  res = [x * x for x in array]
  res.sort()
  return res
