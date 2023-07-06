class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,cursum,n = 0,0,0,len(nums)
        
        minlen = int(1e6)
        while(r < n):
            cursum += nums[r]
            
            while(l <= r and cursum >= target):
                minlen = min(minlen, r - l + 1)
                cursum -= nums[l]
                l += 1                        
            
            r += 1
            
        if(minlen == int(1e6)):
            return 0
        
        return minlen
            
            
        