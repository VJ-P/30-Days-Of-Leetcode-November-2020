class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        num = minutesToTest / minutesToDie + 1
        pigs = 0
        trials = num**pigs
        while trials < buckets:
            pigs += 1
            trials = num**pigs
        
        return pigs