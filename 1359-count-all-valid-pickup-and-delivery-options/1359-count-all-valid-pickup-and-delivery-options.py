class Solution:
    def countOrders(self, n: int) -> int:
        """
        We can assume, a box of size 2n where at one step we have to fill P1 and D1 at any place.
        We have thus 2nC2 way to place the first P-D pair. For second pair P2-D2, (2n - 2) vacant 
        spaces are left. We can thus place the second pair in (2n - 2)C2 ways. Thus so on we can
        multiply all the ways together to get the total ways.
        
        2nC2 x (2n - 2)C2 x (2n - 4)C2 x....x 4C2 x 2C2
        
        So for n = 1
        
        ans = 2C2 = 1
        
        for n = 2
        ans = 4C2 * 2C2 = 4C2 * f(1)
        
        for n = 3
        
        ans = 6C2 * 4C2 * 2C2 = 6C2 * f(2)
        
        """
        M = int(1e9 + 7)
        ans = 1
        
        for i in range(1,n+1):
            ans = (ans * ((2*i)*(2*i - 1))//2)%M
        
        return ans
        