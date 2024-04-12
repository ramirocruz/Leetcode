class Solution {
public:
    int paths[4][2] = {{-1,0}, {1,0}, {0,-1},{0,1}};
    int n,m;
    bool isvalid(int i,int j)
    {
        if(i < 0 || j < 0 || i >=n || j >= m)
            return false;
        return true;
    }
    int dfs(int x,int y, vector<vector<int>>&grid)
    {
        int ans = grid[x][y];
        grid[x][y] = 0;
        for(auto &path:paths)
        {
            int dx = x + path[0];
            int dy = y + path[1];
            if(isvalid(dx,dy) && grid[dx][dy] > 0)
            {
                ans += dfs(dx,dy,grid);
            }
        }
        return ans;
    }
    int findMaxFish(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        int ans = 0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j] > 0)
                {
                    ans = max(ans, dfs(i,j,grid));
                }
            }
        }
        return ans;
    }
};