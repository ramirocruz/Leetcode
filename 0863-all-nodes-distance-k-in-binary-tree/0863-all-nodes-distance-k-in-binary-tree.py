# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchDown(self,root,k):
        if(k == 0):
            self.ans.append(root.val)
            return
        if(root.left):
            self.searchDown(root.left,k-1)
        if(root.right):
            self.searchDown(root.right,k-1)
            
    def helper(self,root):
        if(root == None):
            return -1
        # print("root - {}".format(root.val))
        if(root == self.target):
            # print("target")
            self.searchDown(root,self.k)
            tempval = self.k - 1
            # print('returning {}'.format(tempval))
            return tempval
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        # print("here k={}: {} : {} : {}".format(self.k,root.val,left,right))
        if(left == -1 and right == -1):
            return -1
        
        if(left >= 0):
            
            if(left == 0):
                self.ans.append(root.val)
            elif(root.right != None):
                self.searchDown(root.right,left - 1)
            return left - 1
        
        if(right >= 0):
            if(right == 0):
                self.ans.append(root.val)
            elif(root.left != None):
                self.searchDown(root.left,right - 1)
                
            return right - 1
        
        
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.k = k
        self.ans = []
        self.target = target
        self.helper(root)
        
        return self.ans