class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        i = n-1
        res = 0
        while(i > 0):
            if(nums[i-1] > nums[i]):
                
                #number of elements made from breaking the nums[i-1]
                
                num_elements = (nums[i-1] + nums[i] - 1) // nums[i]
                
                res += num_elements - 1
                
                nums[i-1] = nums[i-1] // num_elements
            
            i -= 1
                
        
        return res
                
        