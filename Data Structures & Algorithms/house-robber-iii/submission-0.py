# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        
        if root.right:
            res += self.rob(root.right.right) + self.rob(root.right.left)

        
        res = max(res, self.rob(root.left) + self.rob(root.right))
    

        return res
        
        

