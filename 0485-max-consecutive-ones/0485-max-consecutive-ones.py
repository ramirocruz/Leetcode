class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen = 0
        idx = 0
        while( idx < len(nums)):
            count = 0
            while(idx < len(nums) and nums[idx] == 1):
                idx += 1
                count += 1
            idx += 1
            
            maxlen = max(maxlen,count)
        
        return maxlen