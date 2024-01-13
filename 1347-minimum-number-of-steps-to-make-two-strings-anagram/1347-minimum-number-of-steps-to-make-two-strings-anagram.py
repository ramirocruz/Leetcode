class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count_s = {}
        char_count_t = {}
        for c in s:
            if c not in char_count_s:
                char_count_s[c] = 1
            else:
                char_count_s[c] += 1
        
        for c in t:
            if c not in char_count_t:
                char_count_t[c] = 1
            else:
                char_count_t[c] += 1
                
        ans = 0
        for c in char_count_s.keys():
            if c not in char_count_t:
                char_count_t[c] = 0
            
            ans += max(char_count_s[c] - char_count_t[c], 0)
        
        return ans