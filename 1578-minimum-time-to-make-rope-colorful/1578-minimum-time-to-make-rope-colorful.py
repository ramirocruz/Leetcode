class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        i = 0
        total_time = 0
        while i < n:
            curcolor = colors[i]
            time_taken = 0
            max_time = neededTime[i]
            while i < n and curcolor == colors[i]:
                max_time = max(max_time,neededTime[i])
                time_taken += neededTime[i]
                i += 1
            # print(curcolor, time_taken,max_time, total_time)
            if(time_taken == max_time):
                continue
            total_time += time_taken - max_time
        return total_time