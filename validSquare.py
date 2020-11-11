class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def helper(p1, p2):
            if p1[0] == p2[0] and p1[1] == p2[1]:
                return False
            
            dx_2 = (p1[0] - p2[0]) ** 2
            dy_2 = (p1[1] - p2[1]) ** 2
            dist = (dx_2 + dy_2) ** 0.5
            unique_lengths.add(dist)
            return True
        
        unique_lengths = set()
        if not(helper(p1, p2)) or not(helper(p1, p3)) or not(helper(p1, p4)) or not(helper(p2, p3)) or not(helper(p2, p4)) or not(helper(p3, p4)):
            return False
        
        return len(unique_lengths) == 2