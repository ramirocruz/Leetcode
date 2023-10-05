class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # there will be max 2 elements more than n/3. 
        elem1 = None
        count1 = 0
        elem2 = None
        count2 = 0
        
        for num in nums:
            if elem1 == num:
                count1 += 1
            elif elem2 == num:
                count2 += 1
            elif count1 == 0:
                elem1 = num
                count1 = 1
            elif count2 == 0:
                elem2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        print(elem1,count1,elem2,count2)
        
        ans = []
        count1 = 0
        count2 = 0
        for num in nums:
            if num == elem1:
                count1 += 1
            elif num == elem2:
                count2 += 1
                
        threshold = len(nums)//3
        print(elem1,count1,elem2,count2)
        if count1 > threshold:
            ans.append(elem1)
        if count2 > threshold:
            ans.append(elem2)
            
        return ans
        
        
        