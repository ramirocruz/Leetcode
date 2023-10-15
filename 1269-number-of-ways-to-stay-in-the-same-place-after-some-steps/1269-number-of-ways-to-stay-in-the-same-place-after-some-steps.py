class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        M = int(1e9 + 7)
        
        arrLen = min(arrLen,steps)
        
        dp = [[-1]*(steps + 1) for _ in range(arrLen)]
        
        def helper(pos,steps):
            if(steps == 0 and pos == 0):
                return 1
            
            if(steps == 0 or pos < 0 or pos == arrLen):
                return 0
            if(dp[pos][steps] != -1):
                return dp[pos][steps]
            
            left = helper(pos - 1,steps - 1)
            right = helper(pos + 1,steps - 1)
            stay = helper(pos,steps - 1)
            
            dp[pos][steps] = (left + right + stay)%M
            
            return dp[pos][steps]
        
        return helper(0,steps)
        