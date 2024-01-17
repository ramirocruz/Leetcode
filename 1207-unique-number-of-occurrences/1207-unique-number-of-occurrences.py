class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f_count = Counter(arr)
        f_set = set(list(f_count.values()))
        return len(f_count.values()) == len(f_set)