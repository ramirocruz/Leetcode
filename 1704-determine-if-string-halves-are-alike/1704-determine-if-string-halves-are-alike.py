class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_count = 0
        def isvowel(c):
            c = c.lower()
            if c in ['a','e','i','o','u']:
                return True
            return False
        
        for idx, c in enumerate(s):
            if isvowel(c):
                if idx < (len(s) // 2):
                    vowel_count += 1
                else:
                    vowel_count -= 1
        
        return vowel_count == 0
                