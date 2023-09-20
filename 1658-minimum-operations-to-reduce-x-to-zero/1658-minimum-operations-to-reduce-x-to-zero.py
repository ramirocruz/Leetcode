class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        n = len(nums)
        total_val = sum(nums)
        val = total_val - x
        
        #we will find total - x in a max subarray.
        
        if val < 0:
            return -1
        
        left,right,cur_sum = 0,0,0
        
        maxlen = -1
        
        while right < n:
            cur_sum += nums[right]
            
            while(left <= right and cur_sum > val):
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum == val:
                maxlen = max(maxlen, right - left + 1)
            
            right += 1
        
        return n - maxlen if maxlen > -1 else -1
            