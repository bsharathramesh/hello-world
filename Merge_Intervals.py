# Merge Intervals

def mergeIntervals(intervals):
    i = 1
    j = 0
    res = []
    intervals.sort(key = lambda i: i[0])
    print(intervals)
    res.append(intervals[0])
    while i < len(intervals):
        if intervals[i][0] <= res[j][1]:
            res[j][1] = max(intervals[i][1],res[j][1])
        else:
            res.append(intervals[i])
            j += 1
        i += 1
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))
        