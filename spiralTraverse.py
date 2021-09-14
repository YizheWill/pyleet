def spiralTraverse(array):
    top, bottom, left, right = 0, len(array) - 1, 0, len(array[0]) - 1
    res = []
    while top <= bottom and left <= right:
        res.extend(array[top][left : right + 1])
        for t in range(top + 1, bottom + 1):
            res.append(array[t][right])

        for r in range(right - 1, left - 1, -1):
            if top == bottom:
                break
            res.append(array[bottom][r])
        for b in range(bottom - 1, top, -1):
            if left == right:
                break
            res.append(array[b][left])
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    return res
