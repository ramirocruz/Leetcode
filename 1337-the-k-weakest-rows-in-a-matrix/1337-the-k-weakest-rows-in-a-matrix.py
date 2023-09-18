class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        temp_list = [0] * len(mat)
        
        for i in range(len(mat)):
            temp_list[i] = (sum(mat[i]),i)
        
        ans = []
        
        temp_list.sort()
        
        ans = [item[1] for item in temp_list[:k]]
        
        # print(ans)
        
        return ans
            
        