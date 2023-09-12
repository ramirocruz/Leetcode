class Solution:
    def minDeletions(self, s: str) -> int:
        fcount = [0]*26
        
        for c in s:
            fcount[ord(c) - ord('a')] += 1
        
        used = set()
        ans = 0
        
        for el in fcount:
            while el > 0 and el in used:
                el -= 1
                ans += 1
            used.add(el)
        
        return ans
        
        