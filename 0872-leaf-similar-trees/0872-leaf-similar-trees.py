# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        st1 = [root1]
        st2 = [root2]
        def isleaf(stack):
            if stack[-1].left == None and stack[-1].right == None:
                return True
            return False
        
        def getleaf(stack):
            if not stack or not isleaf(stack):
                return None
            return stack[-1].val
        
        while st1 and st2:
            while st1 and not isleaf(st1):
                curnode = st1[-1]
                st1.pop()
                if curnode.right:
                    st1.append(curnode.right)
                if curnode.left:
                    st1.append(curnode.left)
            while st2 and not isleaf(st2):
                curnode = st2[-1]
                st2.pop()
                if curnode.right:
                    st2.append(curnode.right)
                if curnode.left:
                    st2.append(curnode.left)
            
            if getleaf(st1) != getleaf(st2):
                return False
            if st1:
                st1.pop()
            if st2:
                st2.pop()
        
        while st1:
            if isleaf(st1):
                return False
            curnode = st1[-1]
            st1.pop()
            if curnode.right:
                st1.append(curnode.right)
            if curnode.left:
                st1.append(curnode.left)
        
        while st2:
            if isleaf(st2):
                return False
            curnode = st2[-1]
            st2.pop()
            if curnode.right:
                st2.append(curnode.right)
            if curnode.left:
                st2.append(curnode.left)
        
        return True
        