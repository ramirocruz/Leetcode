class Solution:
    def minDeletions(self, s: str) -> int:
        fcount = [0]*26
        
        for c in s:
            fcount[ord(c) - ord('a')] += 1
        
        fcount.sort()
        used_idx = set({})
        visited = set({})
        
        ans = 0
        # print(fcount)
        for el in fcount:
            if(el == 0):
                continue
            
            used_idx.add(el)
            
            if el in visited:
                n = el - 1
                while n:
                    if n not in used_idx:
                        used_idx.add(n)
                        ans += el - n
                        break
                    n -= 1
                
                if(n == 0):
                    ans += el
 
            else:
                visited.add(el)
                
        # print(visited)
        # print(used_idx)
        
        return ans
        
        