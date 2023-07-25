class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0,len(arr) - 1
        while(l < r):
            if not (arr[l] < arr[l+1]):
                return l
            l+=1
            
        