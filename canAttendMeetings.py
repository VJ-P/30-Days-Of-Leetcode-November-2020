# class Solution(object):

def canAttendMeetings(intervals):
    if len(intervals) == 1: return True
    intervals.sort(key=lambda x:x[0])
    x2 = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < x2:
            return False
        else:
            x2 = intervals[i][1]


print(canAttendMeetings([[0,30], [15,20], [5,10]]))