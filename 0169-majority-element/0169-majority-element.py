class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = None
        count = 0
        
        for num in nums:
            if major == num:
                count += 1
            elif count == 0:
                major = num
                count = 1
            else:
                count -= 1
        
        return major

            
        