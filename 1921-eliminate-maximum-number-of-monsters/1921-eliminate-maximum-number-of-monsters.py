class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time_taken = [x/y for x,y in zip(dist,speed)]
        time_taken.sort()
        
        res = 0
        print(time_taken)
        for i in range(len(time_taken)):
            if time_taken[i] <= i:
                return res
            
            res += 1
        
        return res