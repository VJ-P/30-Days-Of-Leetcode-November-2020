# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root == None: return 0
        def helper(node):
            
            leftSum = 0
            rightSum = 0
            if node.left != None:
                leftSum = helper(node.left)
            if node.right != None:
                rightSum = helper(node.right)
            
            Sum[0] += abs(leftSum - rightSum)
            return node.val + leftSum + rightSum
        
        Sum = [0]
        helper(root)
        return Sum[0]