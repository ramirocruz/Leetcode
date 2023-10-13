class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {}
        def helper(pos):
            if(pos >= len(cost)):
                return 0
            if pos in dp:
                return dp[pos]
            
            curcost = cost[pos] if pos > -1 else 0
            dp[pos] = curcost + min(helper(pos + 1),helper(pos + 2))
            return dp[pos]
        
        return helper(-1)
        