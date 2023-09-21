class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def upper_bound(nums,item):
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r)//2
                if item < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l
                
            
        def find_element_at(pos):
            left = -int(1e6+1)
            right = int(1e6+1)
            ans = -1
            
            while left < right:
                mid = (left + right)//2
                cnt1 = upper_bound(nums1,mid)
                cnt2 = upper_bound(nums2,mid)
                # print("{} : {} : {} {} : {} {} : {}".format(mid,ans,cnt1,cnt2,left,right,pos))
                if(cnt1 + cnt2 >= pos):
                    ans = mid
                    right = mid
                else:
                    left = mid + 1
            return ans

        n = len(nums1)
        m = len(nums2)
        
        if((n + m)%2):
            medpos = (n+m)//2 + 1
            median = find_element_at(medpos)
            return median
        else:
            medpos1 = (n+m)//2
            medpos2 = medpos1 + 1
            median1 = find_element_at(medpos1)
            median2 = find_element_at(medpos2)
            return (median1+median2)/2
                    
                
        
        