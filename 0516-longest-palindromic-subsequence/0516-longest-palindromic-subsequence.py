class Solution:
    def lcs(self,s1,s2,i,j,dp):
        if(i < 0 or j < 0):
            return 0
        if(dp[i][j] != -1):
            return dp[i][j]
        
        if(s1[i] == s2[j]):
            dp[i][j] = 1 + self.lcs(s1,s2,i-1,j-1,dp)
            return dp[i][j]
        dp[i][j] = max(self.lcs(s1,s2,i-1,j,dp),self.lcs(s1,s2,i,j-1,dp))
        return dp[i][j]
    
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [[-1]*len(s) for _ in range(len(s))]
        lcs = self.lcs(s,s[-1::-1],len(s)-1,len(s) -1,dp)
        return lcs