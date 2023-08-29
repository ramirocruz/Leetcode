class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        curmax = 0
        totmin = n+1
        closingTime = 0
        right_penalty = [0]*(n+1)
        for i in range(n-1,-1,-1):
            
            if(customers[i] == 'Y'):
                curmax += 1
            
            right_penalty[i] = curmax
        
        # print(right_penalty)
        curmax = 0
        for i in range(1,n+1):
            if(customers[i-1] == 'N'):
                curmax += 1
            
            right_penalty[i] += curmax
            totmin = min(totmin,right_penalty[i])
            
        totmin = min(totmin,right_penalty[0])
        
        # print(right_penalty)
        
        for i in range(n+1):
            if(right_penalty[i] == totmin):
                return i
        
        return n+1