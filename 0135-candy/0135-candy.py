class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1]*n
        
        for i in range(0,n-1,1):
            if(ratings[i+1] > ratings[i]):
                ans[i+1] = ans[i] + 1
        
        for i in range(n-1,0,-1):
            if(ratings[i-1] > ratings[i]):
                ans[i-1] = max(ans[i] + 1,ans[i-1])
        
        print(ans)
        return sum(ans)
        