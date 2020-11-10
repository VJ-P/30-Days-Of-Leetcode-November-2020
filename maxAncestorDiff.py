# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def helper(node, currMin, currMax):
            if currMin == None and currMax == None:
                currMin, currMax = node.val, node.val
            else:
                maxDiff[0] = max(maxDiff[0], abs(currMin - node.val), abs(currMax - node.val))
                currMin = min(currMin, node.val)
                currMax = max(currMax, node.val)
            if node.left != None:
                helper(node.left, currMin, currMax)
            if node.right != None:
                helper(node.right, currMin, currMax)
        
        maxDiff = [0]
        helper(root, None, None)
        return maxDiff[0]