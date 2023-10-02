class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        a_count = 0
        b_count = 0
        i = 0
        while i < len(colors):
            cur = colors[i]
            count = 0
            while i < len(colors) and cur == colors[i]:
                i += 1
                count += 1
            
            if count > 2:
                if cur == "A":
                    a_count += count - 2
                else:
                    b_count += count - 2
        
        print(a_count,b_count)
        
        if a_count <= b_count:
            return False
        
        return True
            