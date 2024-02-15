class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prevsum = 0
        persum = -1
        for num in nums:
            if prevsum > num:
                persum = num + prevsum
            prevsum += num
        
        return persum