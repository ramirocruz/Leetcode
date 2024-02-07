class Solution:
    def frequencySort(self, s: str) -> str:
        f_count = Counter(s)
        s_list = list(s)
        s_list.sort(key=lambda x: (-f_count[x],x))
        ans = "".join(s_list)
        return ans