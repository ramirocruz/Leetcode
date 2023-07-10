class Solution:
        
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        left,right = 0,0
        n = len(nums)
        num_zeroes = 0
        ans = 0
        
        while(right < n):
            
            if(nums[right] == 0):
                num_zeroes += 1
            
            while( num_zeroes > 1 ):
                if(nums[left] == 0):
                    num_zeroes -= 1
                left += 1
            
            ans = max(ans,right - left + 1)
            
            right += 1
            
        
        return ans
            
        
        