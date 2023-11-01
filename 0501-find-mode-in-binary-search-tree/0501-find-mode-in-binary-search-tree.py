# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        fcount = {}
        def dfs(root):
            if root == None:
                return
            
            if root.val not in fcount:
                fcount[root.val] = 0
            
            fcount[root.val] += 1
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        res = []
        maxcount = max(fcount.values())
        
        for key,val in fcount.items():
            if val == maxcount:
                res.append(key)
        
        
        return res