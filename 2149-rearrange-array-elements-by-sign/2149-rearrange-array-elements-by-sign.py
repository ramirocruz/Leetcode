class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        evenpos,oddpos = 0,1
        
        for num in nums:
            if num < 0:
                ans[oddpos] = num
                oddpos += 2
            else:
                ans[evenpos] = num
                evenpos += 2
        
        return ans
                
    