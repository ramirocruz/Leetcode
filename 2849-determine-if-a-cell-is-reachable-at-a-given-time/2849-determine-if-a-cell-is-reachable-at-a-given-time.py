class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(fy - sy)
        height = abs(fx - sx)
        
        if width == 0 and height == 0 and t == 1:
            return False
        
        return t >= max(width,height)
        