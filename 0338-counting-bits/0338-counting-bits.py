class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        MSB = 17
        for i in range(n+1):
            count = 0
            for bit in range(MSB+1):
                if((i&(1<<bit))):
                    count += 1
            ans[i] = count
        
        return ans
            
        