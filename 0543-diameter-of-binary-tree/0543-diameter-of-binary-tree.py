# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if root == None:
                return (0, 0)
            
            leftans, leftlen = helper(root.left)
            rightans, rightlen = helper(root.right)
            
            ans = max(leftans,rightans, leftlen + rightlen)
            
            return (ans, max(leftlen, rightlen) + 1)
        
        
        return helper(root)[0]