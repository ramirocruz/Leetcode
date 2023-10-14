class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @cache
        def helper(index, remain):
            
            if remain <= 0:
                return 0
            
            if index >= len(cost):
                return float('inf')
            
            paint = cost[index] + helper(index + 1,remain - time[index] - 1)
            dontPaint = helper(index + 1,remain)
            
            return min(paint,dontPaint)
        
        
        return helper(0,len(cost))