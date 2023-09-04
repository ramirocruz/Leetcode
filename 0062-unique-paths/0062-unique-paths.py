class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = {}
        def fact(num):
            if(num <= 1):
                return 1
            
            if(num in self.dp):
                return self.dp[num]
            
            self.dp[num] = num * fact(num-1)
            
            return self.dp[num]
        nume = fact(m+n-2)
        deno = fact(m-1)*fact(n-1)
        return nume//deno
        