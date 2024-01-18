class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def helper(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in dp:
                return dp[n]
            
            dp[n] = helper(n-1) + helper(n-2)
            return dp[n]
        
        return helper(n)
            