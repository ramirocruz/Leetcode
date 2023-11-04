class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        left_ans = n
        right_ans = n
        
        if len(left) == 0:
            left_ans = 0
        else:
            left_ans = max(left)
        
        if len(right) == 0:
            right_ans = n
        else:
            right_ans = min(right)
        
        return max(n - right_ans, left_ans)
        