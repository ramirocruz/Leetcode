class Solution:
    def totalMoney(self, n: int) -> int:
        
        quotient = n//7
        remainder = n%7
        
        m_7 = ((quotient - 1) * quotient)//2
        s_7 = (7 * 8)//2
        
        ans = s_7 * quotient + m_7 * 7
        ans += ((remainder) * (remainder + 1))//2 + quotient * remainder
        
        return ans
        
        