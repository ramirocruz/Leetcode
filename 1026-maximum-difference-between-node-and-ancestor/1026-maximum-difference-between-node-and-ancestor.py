# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def find_max_diff(node, cur_max_ancestor, cur_min_ancestor):
            if node == None:
                return
            cur_max_ancestor = max(cur_max_ancestor, node.val)
            cur_min_ancestor = min(cur_min_ancestor, node.val)
            diff1 = abs(cur_max_ancestor - node.val)
            diff2 = abs(cur_min_ancestor - node.val)
            self.res = max([self.res, diff1, diff2])
            find_max_diff(node.left, cur_max_ancestor, cur_min_ancestor)
            find_max_diff(node.right, cur_max_ancestor, cur_min_ancestor)
        
        cur_max_ancestor = -1
        cur_min_ancestor = int(1e5 + 1)
        find_max_diff(root, cur_max_ancestor, cur_min_ancestor)
        return self.res
            