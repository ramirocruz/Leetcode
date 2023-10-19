class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        news = []
        newt = []
        
        for char in s:
            if char == '#':
                if len(news):
                    news.pop()
            else:
                news.append(char)
        
        for char in t:
            if char == '#':
                if len(newt):
                    newt.pop()
            else:
                newt.append(char)
                
        return newt == news