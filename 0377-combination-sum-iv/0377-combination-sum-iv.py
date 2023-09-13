class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def helper(cursum):
            
            if(cursum > target):
                return 0
            if(cursum == target):
                return 1
            
            if(cursum in dp):
                return dp[cursum]
            ans = 0
            
            for el in nums:
                ans += helper(cursum + el)
                
            dp[cursum] = ans
            return ans
        
        return helper(0)
            