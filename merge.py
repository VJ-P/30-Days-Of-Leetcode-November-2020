#top: [x1, x2]
#bottom: [y1, y2]

#[ 1 2 3 4 5 ]                
#          [ 6, 7, 8]
# distinct: y1 > x2

#[ 1 2 3 4 5 6 ]                
#          [ 6, 7, 8]
#[ 1 2 3 4 5 ]                
#      [ 4 5 6]
# extend: x2 > y1 and x2 < y2

#[ 1 2 3 4 5 ]                
#      [ 4 5 ]
# contained: y2 <= x2
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]

        for indx in range(1, len(intervals)):
            currI = intervals[indx]
            x1 = ans[-1][0]
            x2 = ans[-1][1]
            y1 = currI[0]
            y2 = currI[1]
            
            if y2 <= x2:
                continue
            elif x2 >= y1 and x2 < y2:
                ans[-1][1] = y2
            else:
                ans.append(currI)
        
        return ans
            
            