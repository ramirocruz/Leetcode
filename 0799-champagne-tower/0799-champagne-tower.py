class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*row for row in range(1,102)]
        
        dp[0][0] = poured
        
        for row in range(query_row+1):
            for col in range(row + 1): 
                # traversing each glass row-wise
                glassval = (dp[row][col] - 1)/2
                if glassval > 0:
                    dp[row+1][col] += glassval
                    dp[row+1][col+1] += glassval
        
        
        return min(1,dp[query_row][query_glass])
        
        