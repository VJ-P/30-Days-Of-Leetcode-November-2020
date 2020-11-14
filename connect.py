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
        
        queue = [root]
        
        j = 1
        breadthLength = 2 ** 0
        
        while len(queue) > 0:
            current = queue.pop(0)
            if j == breadthLength:
                current.next = None
                breadthLength = breadthLength*2
                j = 1
            else:
                current.next = queue[0]
                j += 1
            
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)

        return root