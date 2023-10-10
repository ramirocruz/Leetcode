class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        uniqueNums = sorted(set(nums)) #sorted unique elements
        n = len(nums)
        
        def upper_bound(target):
            l,r = 0, len(uniqueNums) - 1
            ans = r + 1
            while l <= r:
                mid = (l + r)//2
                if uniqueNums[mid] > target:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
                
            return ans
        
        ans = n
        
        for idx,elem in enumerate(uniqueNums):
            left = elem
            right = elem + n - 1
            less_than_left = idx #elements on the left side of the range
            less_than_right = upper_bound(right) #elements smaller or equal to right
            nums_in_range = less_than_right - less_than_left
            
            op_cost = n - nums_in_range
            
            # print(idx,elem,right,less_than_right,nums_in_range,op_cost)
        
            ans = min(ans,op_cost)
        
        return ans
            
            
        