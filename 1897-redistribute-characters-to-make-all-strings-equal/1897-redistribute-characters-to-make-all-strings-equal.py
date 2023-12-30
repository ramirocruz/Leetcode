class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        char_count = {}
        for word in words:
            for c in word:
                if c not in char_count:
                    char_count[c] = 0
                char_count[c] += 1
        
        for val in char_count.values():
            if val % n != 0:
                return False
        
        return True