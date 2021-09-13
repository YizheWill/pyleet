def minimumWaitingTime(queries):
    # # Write your code here.
    # queries.sort()
    # res = []
    # queries = queries[0:-1]
    # print(queries)
    # for item in queries:
    #     res.append((res[-1] if len(res) > 0 else 0) + item)
    # return res
    # Write your code here.
    queries.sort()
    res, result = 0, 0
    for item in queries[0:-1]:
        res += item
        result += res
    return result


if __name__ == '__main__':
    test = [3, 2, 1, 2, 6]
    minimumWaitingTime(test)
