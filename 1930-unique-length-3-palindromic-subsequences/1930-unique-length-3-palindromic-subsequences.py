class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = {}
        right = {}
        ans = 0
        for idx,c in enumerate(s):
            if c not in left:
                left[c] = idx
            else:
                right[c] = idx
        
        common_chars = left.keys() & right.keys()
        
        for c in common_chars:
            unique_count = set()
            for i in range(left[c] + 1,right[c]):
                unique_count.add(s[i])
            
            ans += len(unique_count)

        return ans