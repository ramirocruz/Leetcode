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
       
        left = max(1,floor(max_time/hour))
        right = int(max(max(dist),ceil(dist[-1]/(hour - min_time))))
        
        ans = -1
        # print(left,right)
        while(left <= right):
            mid = (left + right)//2
            time_taken = get_time(mid)
            
            if(time_taken > hour):
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
            
        return ans
        