bool isvalid(int i,int j,int n, int m)
{
    if(i < 0 || j < 0 || i >= n || j >= m)
        return false;
    return true;
}
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>>dist(n,vector<int>(m,-1));
        queue<array<int,2>>Q;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j] == 2)
                {
                    Q.push({i,j});
                    dist[i][j] = 0;
                }
            }
        }
        int res = 0;
        int paths[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        while(Q.size())
        {
            auto data = Q.front();
            int x = data[0], y = data[1];
            Q.pop();
            for(auto &path:paths)
            {
                int dx = x + path[0];
                int dy = y + path[1];
                if(isvalid(dx,dy,n,m) && dist[dx][dy] == -1 && grid[dx][dy] == 1)
                {
                    dist[dx][dy] = dist[x][y] + 1;
                    grid[dx][dy] = 2;
                    res = max(res, dist[dx][dy]);
                    Q.push({dx,dy});
                }
                
            }
        }
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j] == 1)
                    return -1;
            }
        }
        
        return res;
    }
};