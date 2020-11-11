class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            k = len(A[i]) - 1
            j = 0
            while k > j:
                A[i][j], A[i][k] = A[i][k], A[i][j]
                k -= 1
                j += 1
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = 1 if A[i][j] == 0 else 0
        return A