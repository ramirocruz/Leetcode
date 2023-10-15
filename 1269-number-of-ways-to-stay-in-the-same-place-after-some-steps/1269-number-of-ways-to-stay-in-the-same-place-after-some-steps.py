class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        # dp = [[-1]*501 for _ in range(arrLen + 1) ]
        M = int(1e9 + 7)
        @cache
        def helper(pos,steps):
            if(steps == 0 and pos == 0):
                return 1
            
            if(steps == 0 or pos < 0 or pos == arrLen):
                return 0
            
            left = helper(pos - 1,steps - 1)
            right = helper(pos + 1,steps - 1)
            stay = helper(pos,steps - 1)
            
            return (left + right + stay)%M
        
        return helper(0,steps)
        