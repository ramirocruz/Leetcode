class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        def issubset(f_word,f_target):
            for char, cnt in f_word.items():
                if char not in f_target:
                    return False
                if cnt > f_target[char]:
                    return False
            return True
        
        def get_f_count(word):
            f_count = {}
            for c in word:
                if c not in f_count:
                    f_count[c] = 1
                else:
                    f_count[c] += 1
            
            return f_count
        
        f_target = get_f_count(chars)
        
        ans = 0
        for word in words:
            f_word = get_f_count(word)
            if issubset(f_word,f_target):
                ans += len(word)
        
        return ans
        