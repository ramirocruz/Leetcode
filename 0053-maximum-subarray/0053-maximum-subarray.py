class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = int(-1e4 - 1)
        cursum = 0
        for x in nums:
            cursum += x
            
            if(cursum > maxsum):
                maxsum = cursum
            if(cursum < 0):
                cursum = 0
            
        return maxsum
        