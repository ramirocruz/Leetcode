class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        one_count = [0]*n
        for idx,row in enumerate(bank):
            for elem in row:
                if elem == "1":
                    one_count[idx] += 1
        
        ans = 0
        idx = 0
        prev = 0
        while idx < n:
            while idx < n and one_count[idx] == 0:
                idx += 1
            if idx == n:
                break
            cur = one_count[idx]
            ans += prev * cur
            idx += 1
            prev = cur
        
        return ans
            
            
            
            
                    
            