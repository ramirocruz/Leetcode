class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        prevRow = [0]*(rowIndex + 1)
        curRow = [0]*(rowIndex + 1)
        ans = []
        for row in range(rowIndex + 1):
            ncol = row + 1
            col = 0
            while col < ncol:
                if col == 0:
                    curRow[col] = 1
                else:
                    curRow[col] = prevRow[col-1] + prevRow[col]    
                col += 1
                
            for i in range(ncol):
                prevRow[i] = curRow[i]
                
        
        return curRow
        
                
            
        