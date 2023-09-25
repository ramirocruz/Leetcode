class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_fcount = [0]*26
        t_fcount = [0]*26
        
        for c in s:
            s_fcount[ord(c) - ord('a')] += 1
        for c in t:
            t_fcount[ord(c) - ord('a')] += 1
            
        for i in range(26):
            if (t_fcount[i] > s_fcount[i]):
                return chr(i + ord('a'))
            
        return ""
        