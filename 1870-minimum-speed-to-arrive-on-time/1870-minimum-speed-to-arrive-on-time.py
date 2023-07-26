class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        min_time = len(dist) - 1
        max_time = sum(dist)
        
        
        if(hour <= min_time):
            return -1
        

        
        def get_time(speed):
            t = 0
            for el in dist[:-1]:
                t += ceil(el/speed)
            t += dist[-1]/speed
            return t
       
        left = 1
        right = int(1e7+1)
        
        ans = -1
        
        while(left <= right):
            mid = (left + right)//2
            time_taken = get_time(mid)
            
            if(time_taken > hour):
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
            
        return ans
        