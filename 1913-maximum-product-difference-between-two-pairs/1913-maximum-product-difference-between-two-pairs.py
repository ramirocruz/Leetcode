class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        w = nums[-1]
        x = nums[-2]
        y = nums[0]
        z = nums[1]
        
        return w*x - y*z