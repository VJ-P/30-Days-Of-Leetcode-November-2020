"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None
        bfsOrder = []
        queue = [root]
        
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
            bfsOrder.append(current)
        
        num = 0
        i = 0
        j = 1
        breadthLength = 2 ** num
        while i < len(bfsOrder):
            if j == breadthLength:
                bfsOrder[i].next = None
                breadthLength = breadthLength*2
                j = 1
            else:
                bfsOrder[i].next = bfsOrder[i + 1]
                j += 1
            i += 1
        return root