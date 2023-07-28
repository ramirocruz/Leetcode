class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        n = len(nums)

        def maxDiff(left,right):
            if(left == right):
                return nums[left]
            
            left_el_taken = nums[left] - maxDiff(left+1,right)
            
            right_el_taken = nums[right] - maxDiff(left,right-1)
            
            return max(left_el_taken,right_el_taken)
        
        return maxDiff(0,n-1) >= 0
            
        