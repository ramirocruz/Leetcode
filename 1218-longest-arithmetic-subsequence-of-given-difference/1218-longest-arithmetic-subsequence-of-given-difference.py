class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        maxlen = 1
        for x in arr:
            if((x - difference) not in dp):
                dp[x] = 1
            else:
                dp[x] = dp[x - difference] + 1
                
            maxlen = max(maxlen,dp[x])
        
        return maxlen
            
                
            
        