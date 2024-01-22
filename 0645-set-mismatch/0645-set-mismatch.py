class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        f_count = Counter(nums)
        n = len(nums)
        
        ans = [-1,-1]
        for num in range(1,n+1):
            if num not in f_count:
                ans[1] = num
            elif f_count[num] == 2:
                ans[0] = num
        return ans