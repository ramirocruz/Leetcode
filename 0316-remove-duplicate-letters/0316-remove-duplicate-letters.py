class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurance = {c:i for i,c in enumerate(s)}
        
        print(last_occurance)
        
        for i,c in enumerate(s):
            if c not in seen:
                while stack and stack[-1] > c and last_occurance[stack[-1]] > i:
                    seen.remove(stack[-1])
                    stack.pop()
                    
                seen.add(c)
                stack.append(c)

        return "".join(stack)
        