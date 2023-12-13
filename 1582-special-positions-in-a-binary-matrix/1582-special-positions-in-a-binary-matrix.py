class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        row_1_cnt = [0]*n
        col_1_cnt = [0]*m


        for i in range(n):
            for j in range(m):
                row_1_cnt[i] += mat[i][j]
        
        for j in range(m):
            for i in range(n):
                col_1_cnt[j] += mat[i][j]
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == row_1_cnt[i] == col_1_cnt[j] == 1:
                    ans += 1
        
                
        return ans