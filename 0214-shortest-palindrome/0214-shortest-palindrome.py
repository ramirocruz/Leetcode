class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def z_func(s):
            z = [0]*len(s)
            left = 0
            right = 0
            for i in range(1,len(s)):
                if(i < right):
                    z[i] = min(right - i, z[i - left])
                    
                while(i + z[i] < len(s) and s[z[i]] == s[i + z[i]]):
                    z[i] += 1
                
                if( i + z[i] > right):
                    right = i + z[i]
                    left = i
            return z
        
        revs = s[-1::-1]
        temps = s + '#' + revs
        z = z_func(temps)
        
        # print(temps, z)
        l = 1
        for i in range(len(s),len(temps)):
            if(z[i] == len(temps) - i):
                l = z[i]
                break
                
        # print(l)
        pre = s[-1:l-1:-1]
        # print(pre)
        
        return pre+s
        
                