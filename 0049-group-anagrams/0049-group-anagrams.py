class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            og_word = word
            word = "".join(sorted(word))
            if word not in anagram_map:
                anagram_map[word] = []
                
            anagram_map[word].append(og_word)
        return list(anagram_map.values())