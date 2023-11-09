class Solution:
    def countHomogenous(self, s: str) -> int:
        M = int(1e9 + 7)
        
        i = 0
        res = 0
        while i < len(s):
            cur = s[i]
            cnt = 0
            while i < len(s) and cur == s[i]:
                i += 1
                cnt += 1
            
            res += (cnt*(cnt + 1))//2
            res %= M
        
        
        return res