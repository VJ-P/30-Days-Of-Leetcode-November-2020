class Solution(object):
    # def twoSumLessThanK(self, A, K): #O(n^2)
    #     ans = -1
    #     for i in range(len(A)):
    #         for j in range(i+1, len(A)):
    #             if A[i] + A[j] < k:
    #                 ans = max(ans, A[i] + A[j])
    #     return ans

    def twoSumLessThanK(self, A, K):#O(nlogn)
        ans = -1
        lPntr = 0
        rPntr = len(A)-1
        A.sort()
        while(lPntr < rPntr):
            S = A[lPntr] + A[rPntr]
            if S < K and S > ans:
                ans = S
            elif S > K:
                rPntr -= 1
            else:
                lPntr += 1
        return ans

# A = [34, 23, 1, 24, 75, 33, 54, 8]
# k = 60

# print(twoSumLessThanK(A, k))

# A = [10, 20, 30]
# k = 15

# print(twoSumLessThanK(A, k))