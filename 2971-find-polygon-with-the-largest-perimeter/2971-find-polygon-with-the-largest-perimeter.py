class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prevsum = 0
        persum = -1
        for num in nums:
            if num < prevsum:
                persum = num + prevsum
            prevsum += num
        
        return persum