class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        sum_by_formula = (n * (n + 1))//2
        return sum_by_formula - total