class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                prod = max(dp[i - j] * dp[j],(i-j)*j,dp[i -j]*(j),(i-j)*dp[j])
                dp[i] = max(dp[i],prod)
        
        
        print(dp)
        
        return dp[n]
                
        