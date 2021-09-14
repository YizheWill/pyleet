def stupidMergeOverlappingIntervals(intervals):
    res = []
    intervals.sort(key=lambda x: (x[0], x[1]))
    prev = intervals[0]
    for i in range(len(intervals) - 1):
        if intervals[i + 1][0] <= prev[-1]:
            if intervals[i + 1][1] > prev[-1]:
                prev[-1] = intervals[i + 1][1]
            else:
                continue
        else:
            res.append(prev)
            prev = intervals[i + 1]
    res.append(prev)
    return res
# this approach is too stupid....
# and it's done by me....
# but answer is not much smarter either...

# 思路应该是先考虑好，无论如何，第一个要放进去，如果放进去了，那么就要对他的尾部进行修改。


def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    curr_interval = intervals[0]
    result = [curr_interval]

    for next_interval in intervals:
        nextstart, nextend = next_interval
        currstart, currend = curr_interval
        if nextstart <= currend:
            curr_interval[1] = max(nextend, currend)
        else:
            curr_interval = next_interval
            result.append(curr_interval)
    return result
