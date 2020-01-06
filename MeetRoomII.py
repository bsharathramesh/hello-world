# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# Example 1:
    # Input: [[0, 30],[5, 10],[15, 20]]
    # Output: 2
# Example 2:
    # Input: [[7,10],[2,4]]
    # Output: 1

def minMeetingRooms(intervals):
    if not intervals:
        return 0 
    s_ptr = []
    e_ptr = []
    s_ptr = ([intervals[i][0] for i in range(len(intervals))])
    e_ptr = ([intervals[i][1] for i in range(len(intervals))])
    s_ptr.sort()
    e_ptr.sort()

    # start counter and the end counter
    sc = 0
    ec = 0
    used_rooms = 0

    length = len(intervals)
    while sc < length:
        if s_ptr[sc] >= e_ptr[ec]:
            used_rooms -= 1
            ec += 1
        used_rooms += 1
        sc += 1
    return used_rooms


Input = [[0, 30],[5, 10],[15, 20]]
print(minMeetingRooms(Input))
