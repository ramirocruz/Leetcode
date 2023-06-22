class Solution:
    def z_func(self,s: str):
        n = len(s)
        z = [0]*n
        for i in range(1,n):
            l = 0
            r = 0
            if(i < r):
                z[i] = min(z[i - l],r - i)
            while(i+z[i] < n and s[i + z[i]] == s[z[i]]):
                z[i] += 1
            
            if(i+z[i] > r):
                l = i
                r = i + z[i]
        return z
    
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        merged_string = needle + '#' + haystack
        z = self.z_func(merged_string)
        for i in range(len(z)):
            if(z[i] == n):
                return i - n - 1;
        return -1
        
        
        