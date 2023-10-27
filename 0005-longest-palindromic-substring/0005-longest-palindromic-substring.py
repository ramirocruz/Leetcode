class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = 0
        res = ""
        i = 0
        while i < len(s):
            j = 0
            while i - j > -1 and i + j < len(s) and s[i-j] == s[i + j]:
                j += 1
                
            if 2*j - 1 > ans:
                res = s[i - j + 1: i + j]
                ans = 2*j - 1
            
            j = 0
            
            while i - j > -1 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                j += 1
                
            if 2*j > ans:
                res = s[i - j + 1: i + j + 1]
                ans = 2*j
            
            i += 1
        
        
        return res
        