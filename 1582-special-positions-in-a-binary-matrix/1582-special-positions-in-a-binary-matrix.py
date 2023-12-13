class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        row_1_cnt = [0]*n
        col_1_cnt = [0]*m


        for row in range(n):
            for col in range(m):
                row_1_cnt[row] += mat[row][col]
                col_1_cnt[col] += mat[row][col]
        
        ans = 0
        
        for row in range(n):
            if row_1_cnt[row] == 1:
                for col in range(m):
                    if col_1_cnt[col] == mat[row][col] == 1:
                        ans += 1
                        break
        
                
        return ans