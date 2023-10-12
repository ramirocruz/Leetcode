# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def get_peak():
            l = 0
            r = mountain_arr.length() - 1
            res = -1
            while(l <= r):
                mid = (l + r)//2
                
                if(mountain_arr.get(mid) > mountain_arr.get(mid + 1)):
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res
        
        
        def bs(start,end):
            l = start
            r = end
            res = -1
            while(l <= r):
                mid = (l + r)//2
                mid_val = mountain_arr.get(mid)
                if(target == mid_val):
                    return mid
                elif(target > mid_val):
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return res
        
        def reverse_bs(start,end):
            l = start
            r = end
            res = -1
            while(l <= r):
                mid = (l + r)//2
                mid_val = mountain_arr.get(mid)
                if(target == mid_val):
                    return mid
                elif(target < mid_val):
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return res
        
        
        peak = get_peak()
        
        res = bs(0,peak)
        
        if res == -1:
            
            return reverse_bs(peak+1,mountain_arr.length() - 1)
        
        
        return res