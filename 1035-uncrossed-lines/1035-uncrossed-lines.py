class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        n,m = len(nums1),len(nums2)
        dp = [[None]*m for _ in range(n)]
        
        def lcs(i,j):
            if i <0 or j < 0:
                return 0
            if dp[i][j] != None:
                return dp[i][j]
            
            if nums1[i] == nums2[j]:
                
                dp[i][j] = lcs(i-1,j-1) + 1
            
            else:
                dp[i][j] = max(lcs(i-1,j),lcs(i,j-1))
            
            return dp[i][j]
        
        
        return lcs(n-1,m-1)
        