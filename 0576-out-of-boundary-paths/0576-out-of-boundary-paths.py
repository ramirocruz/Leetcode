class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        def isOut(i,j):
            if (i < 0 or j < 0 or i >= m or j >= n):
                return True
            return False
        
        dp = [[[-1]*(maxMove+1) for _ in range(n)] for _ in range(m)]
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        MOD = int(1e9 + 7)

        def dfs(i,j, maxMove):
            if isOut(i,j):
                return 1
            if maxMove == 0:
                return 0
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            res = 0
            for move in moves:
                dx, dy = move
                res = (res + dfs(i + dx, j + dy, maxMove - 1))%MOD
            
            dp[i][j][maxMove] = res
            return res
        
        return dfs(startRow, startColumn, maxMove)

                