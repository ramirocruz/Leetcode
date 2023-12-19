class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        def isvalid(i,j):
            if(i < 0 or j < 0 or i >=n or j >= m):
                return False
            return True
        
        def get_avg(i,j):
            paths = [[0,-1],[0,1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
            total_cnt = 1
            total_sum = img[i][j]
            for path in paths:
                x = i + path[0]
                y = j + path[1]
                if isvalid(x,y):
                    total_cnt += 1
                    total_sum += img[x][y]
            
            return total_sum // total_cnt
        
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = get_avg(i,j)
        
        return ans