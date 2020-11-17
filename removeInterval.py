class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
                i += 1
            elif interval[0] >= toBeRemoved[0] and interval[1] <= toBeRemoved[1]:
                intervals.pop(i)
            elif interval[0] < toBeRemoved[0] and interval[1] > toBeRemoved[1]:
                if i == len(interval) - 1:
                    intervals.append([toBeRemoved[1], interval[1]])
                    interval[1] = toBeRemoved[0]
                    break
                else:
                    intervals.insert(i+1, [toBeRemoved[1], interval[1]])
                    interval[1] = toBeRemoved[0]
                    i += 2
            elif interval[1] > toBeRemoved[0] and interval[0] < toBeRemoved[0]:
                interval[1] = toBeRemoved[0]
                i += 1
            elif interval[0] < toBeRemoved[1] and interval[1] > toBeRemoved[1]:
                interval[0] = toBeRemoved[1]
                i += 1
        
        return intervals