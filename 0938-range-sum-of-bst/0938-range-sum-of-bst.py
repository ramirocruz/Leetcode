# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def low_sum(root):
            if root == None:
                return 0
            if root.val < low:
                return low_sum(root.right)
            if root.val > high:
                return low_sum(root.left)
            
            return root.val + low_sum(root.right) + low_sum(root.left)
        
        return low_sum(root)