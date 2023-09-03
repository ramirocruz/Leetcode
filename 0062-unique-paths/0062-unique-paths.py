class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def fact(num):
            if(num <= 1):
                return 1
            
            if(num in dp):
                return dp[num]
            
            dp[num] = num * fact(num-1)
            
            return dp[num]
        nume = fact(m+n-2)
        deno = fact(m-1)*fact(n-1)
        return nume//deno
        