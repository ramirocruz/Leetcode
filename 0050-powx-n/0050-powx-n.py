class Solution:
    def helper(self,x,n):
        if(x == 0):
            return 0
        
        if(n == 1):
            return x
        
        if(n == 0):
            return 1
        
        if(n%2 == 0):
            temp_mult = self.helper(x,n/2)
            return temp_mult*temp_mult
        
        mult = self.helper(x,(n-1)/2)
        return x * mult * mult
        
        
    def myPow(self, x: float, n: int) -> float:
        
        if(n >= 0):
            return self.helper(x,n)
        
        return 1/self.helper(x,-n);
        
        
    
        