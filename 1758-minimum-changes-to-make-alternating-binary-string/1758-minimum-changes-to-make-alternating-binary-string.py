class Solution:
    def minOperations(self, s: str) -> int:
        type_one_diff = 0
        type_two_diff = 0
        n = len(s)
        type_one = "10"*(n//2) + "1" * (n%2)
        type_two = "01"*(n//2) + "0" * (n%2)
        for i in range(len(s)):
            if s[i] != type_one[i]:
                type_one_diff += 1
            
            if s[i] != type_two[i]:
                type_two_diff += 1
        
        return min(type_one_diff,type_two_diff)
            
            