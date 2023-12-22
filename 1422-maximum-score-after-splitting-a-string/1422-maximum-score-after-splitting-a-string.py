class Solution:
    def maxScore(self, s: str) -> int:
        zero_count = 0
        one_count = 0
        
        for i in range(1,len(s)):
            if s[i] == '1':
                one_count += 1
        ans = 0
        for i in range(len(s)-1):
            zero_count += 1 if s[i] == '0' else 0
            ans = max(ans,zero_count + one_count)
            one_count -= 1 if s[i + 1] == '1' else 0
        
        return ans