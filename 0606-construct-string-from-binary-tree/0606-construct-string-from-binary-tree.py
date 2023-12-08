# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def helper(root):
            if root is None:
                return ""
            
            if root.left is None and root.right is None:
                return str(root.val)
            
            res = str(root.val)
            lstr = helper(root.left)
            rstr = helper(root.right)
            
            if len(lstr) == 0:
                res += "()"
            else:
                res += "(" + lstr + ")"
            
            if len(rstr):
                res += "(" + rstr + ")"
            
            return res
        
        return helper(root)
            
            