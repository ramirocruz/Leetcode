class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        ans = pref[:]
        
        for i in range(1,len(pref)):
            ans[i] = pref[i] ^ pref[i - 1]
            
        
        return ans
        