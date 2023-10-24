# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        Q = deque()
        Q.append(root)
        
        ans = []
        
        while Q:
            level_len = len(Q)
            maxval = float('-inf')
            while level_len:                
                node = Q.popleft()
                maxval = max(maxval,node.val)
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                    
                level_len -= 1
            
            ans.append(maxval)
        
        return ans
        