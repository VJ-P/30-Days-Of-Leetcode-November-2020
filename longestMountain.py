class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ans = 0
        
        for i in range(1, len(A)-1):
            if A[i] > A[i+1] and A[i] > A[i-1]:
                j = i - 1 
                k = i + 1
                
                while j > 0 and A[j] > A[j-1]:
                    j -= 1
                
                while k < len(A)-1 and A[k] > A[k+1]:
                    k += 1
                ans = max(ans, k-j+1)
        return ans