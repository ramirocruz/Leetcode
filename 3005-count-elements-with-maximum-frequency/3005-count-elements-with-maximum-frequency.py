class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f_count = Counter(nums)
        total_freq = 0
        max_freq = max(f_count.values())
        
        for val in f_count.values():
            if val == max_freq:
                total_freq += max_freq
        
        return total_freq