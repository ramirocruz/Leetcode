class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f_count_1 = {}
        f_count_2 = {}
        for c in word1:
            if c not in f_count_1:
                f_count_1[c] = 1
            else:
                f_count_1[c] += 1
        for c in word2:
            if c not in f_count_2:
                f_count_2[c] = 1
            else:
                f_count_2[c] += 1
        
        
        word1 = sorted(word1)
        word2 = sorted(word2)
        
        if word1 == word2:
            return True
        if sorted(f_count_1.keys()) == sorted(f_count_2.keys()):
            word1_vals = sorted(f_count_1.values())
            word2_vals = sorted(f_count_2.values())
            return word1_vals == word2_vals
        return False