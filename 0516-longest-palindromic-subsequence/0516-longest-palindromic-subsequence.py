class Solution:
    
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [[-1]*len(s) for _ in range(len(s))]
        def lps(l,r):
            if(dp[l][r] != -1):
                return dp[l][r]
            if(l > r):
                return 0
            if(l == r):
                return 1
            if(s[l] == s[r]):
                dp[l][r] = lps(l+1,r-1) + 2
            else:
                dp[l][r] = max(lps(l,r-1),lps(l+1,r))
            
            return dp[l][r]
        

        return lps(0,len(s) - 1)