def runLengthEncoding(string):
    # Write your code here.
    res = ''
    i = 0
    while i < len(string):
        counter, idx = counterHelper(string, i)
        res += translateBigNumber(counter, string[i])
        i = idx
    return res


def counterHelper(array, idx):
    counter = 1
    for i in range(idx, len(array) - 1):
        if array[i + 1] == array[i]:
            counter += 1
        else:
            return [counter, i + 1]
    return [counter, len(array)]


def translateBigNumber(counter, char):
    q = counter // 9 if counter > 9 else 0
    r = counter % 9 if counter > 9 else counter % 10
    return q * f'9{char}' + f'{r}{char}'
