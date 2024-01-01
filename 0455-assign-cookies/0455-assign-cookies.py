class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        ans = 0
        i,j = 0,0
        while i < len(g):
            child = g[i]
            while j < len(s) and s[j] < child:
                j += 1
            if j == len(s):
                break
            ans += 1
            i += 1
            j += 1
        
        return ans