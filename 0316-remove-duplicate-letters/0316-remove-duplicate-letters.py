from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        fcount = Counter(s)

        for i,c in enumerate(s):
            fcount[c] -= 1
            
            if c in visited:
                continue
                
            while stack and stack[-1] > c and fcount[stack[-1]]:
                visited.remove(stack[-1])
                stack.pop()
            
            visited.add(c)
            stack.append(c)
                

        return "".join(stack)
        