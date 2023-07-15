class Solution:
    
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[-1]*n for _ in range(k+1)]
        
        def helper(count,pos,ed_time):
            if(pos == n or count == k):
                return 0
            
            if(events[pos][0] <= ed_time):
                # dp[count][pos] = helper(count,pos+1,ed_time)
                # return dp[count][pos]
                return helper(count,pos+1,ed_time)
            
            if(dp[count][pos] != -1):
                return dp[count][pos]


            ans =  max(helper(count,pos+1,ed_time),events[pos][2] + helper(count + 1,pos+1,events[pos][1]))

            dp[count][pos] = ans
            return ans
    
        return helper(0,0,-1)
    
        