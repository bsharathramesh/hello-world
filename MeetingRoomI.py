# Meeting Room I
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# Example 1:
    # Input: [[0,30],[5,10],[15,20]]
    # Output: false
# Example 2:
    # Input: [[7,10],[2,4]]
    # Output: true

def mergeIntervals(intervals):
    if not intervals:
        return True
    i = 1
    j = 0
    res = []
    intervals.sort(key = lambda i: i[0])
    res.append(intervals[0])
    while i < len(intervals):
        if intervals[i][0] <= res[j][1]:
            res[j][1] = max(intervals[i][1],res[j][1])
        else:
            res.append(intervals[i])
            j += 1
        i += 1
    if len(intervals) == len(res):
        return True
    else:
        return False

Input = []
print(mergeIntervals(Input))
