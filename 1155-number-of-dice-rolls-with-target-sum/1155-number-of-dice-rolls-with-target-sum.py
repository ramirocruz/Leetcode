class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = int(1e9 + 7)
        dp = [[-1]*(target + 1) for _ in range(n + 1)]
        def waysToTarget(dice_idx,currsum):
            if (dice_idx == n):
                return currsum == target
            
            if (dp[dice_idx][currsum] != -1):
                return dp[dice_idx][currsum]
            
            ways = 0
            
            for i in range(1,min(k,target-currsum) + 1):
                ways = (ways + waysToTarget(dice_idx+1,currsum + i)) % MOD
            
            dp[dice_idx][currsum] = ways
            return ways
        
        return waysToTarget(0,0)