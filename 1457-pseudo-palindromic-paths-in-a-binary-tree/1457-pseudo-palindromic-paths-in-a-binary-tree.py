# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        f_count = Counter()
        def checkpalindrome():
            odd_count = 0
            even_count = 0
            total_count = 0
            for val in f_count.values():
                total_count += val
                if val % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            if total_count % 2 == 0:
                return not odd_count
            else:
                return odd_count == 1
            
        def helper(node):
            if node == None:
                return 0
            f_count[node.val] += 1
            ans = 0
            if node.left == None and node.right == None:
                # print(f_count)
                if checkpalindrome():
                    # print("here")
                    ans = 1
                f_count[node.val] -= 1
                return ans
            
            ans += helper(node.left) + helper(node.right)
            f_count[node.val] -= 1
            return ans
        
        return helper(root)