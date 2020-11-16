# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def helper(node):
            if node.val > low and node.left: helper(node.left)
            if node.val >= low and node.val <= high:
                sumNodes[sum] += node.val
            if node.val < high and node.right: helper(node.right)                
        
        sumNodes = {sum: 0}
        helper(root)
        return sumNodes[sum]