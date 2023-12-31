class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}
        ans = -1
        for idx, c in enumerate(s):
            if c not in char_map:
                char_map[c] = []
            char_map[c].append(idx)
        
        for val in char_map.values():
            ans = max(ans,val[-1] - val[0] - 1)
        
        return ans