class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        l,r = 0, len(nums) - 1
        while l < r:
            pair_sum = nums[l] + nums[r]
            ans = max(ans,pair_sum)
            l += 1
            r -= 1
        
        return ans