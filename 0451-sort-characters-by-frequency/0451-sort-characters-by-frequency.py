class Solution:
    def frequencySort(self, s: str) -> str:
        f_count = Counter(s)
        sorted_list = sorted(f_count.items(),key=lambda x: -x[1])
        ans = ""
        for key, val in sorted_list:
            ans += key*val
        
        return ans