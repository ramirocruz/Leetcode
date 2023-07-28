class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]

        def maxDiff(left,right):
            if(left == right):
                return nums[left]
            
            if(dp[left][right] != -1):
                return dp[left][right]
    
            left_el_taken = nums[left] - maxDiff(left+1,right)
            
            right_el_taken = nums[right] - maxDiff(left,right-1)
            
            dp[left][right] = max(left_el_taken,right_el_taken)
            
            return dp[left][right]
        
        return maxDiff(0,n-1) >= 0
            
        