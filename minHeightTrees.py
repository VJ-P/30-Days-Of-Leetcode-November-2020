class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        
        ans = []
        degree = [0]*n
        adjList = {}
        
        for i in range(n):
            adjList[i] = []
        
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        #print(adjList)
        
        for i in range(n):
            if degree[i] == 1:
                ans.append(i)
        
        while n > 2:
            size = len(ans)
            n -= size
            
            while size > 0:
                for i in adjList[ans.pop(0)]:
                    degree[i] -= 1
                    if degree[i] == 1:
                        ans.append(i)
                size -= 1
        return ans
            
            
        