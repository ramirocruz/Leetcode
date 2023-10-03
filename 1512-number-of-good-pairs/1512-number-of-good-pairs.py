class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        nums.sort()
        while i < len(nums):
            cur = nums[i]
            cnt = 0
            while i < len(nums) and cur == nums[i]:
                i += 1
                cnt += 1
            
            ans += (cnt * (cnt - 1))//2
        
        return ans
        