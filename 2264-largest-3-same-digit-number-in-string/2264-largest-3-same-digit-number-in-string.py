class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ""
        
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                if num[i:i+3] > ans:
                    ans = num[i:i+3]
        
        return ans
        