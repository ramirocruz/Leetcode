bool isvalid(int i,int j,int n,int m)
{
    if(i < 0 || j < 0 || i >= n || j >= m)
        return false;
    return true;
}
class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<bool>>visited(n, vector<bool>(m, false));
        queue<array<int,3>>Q;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j] == 1)
                {
                    Q.push({i,j,0});
                    visited[i][j] = true;
                }
            }
        }
        int paths[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        int ans = -1;
        while(Q.size())
        {
            auto data = Q.front();
            int x = data[0];
            int y = data[1];
            int d = data[2];
            Q.pop();
            
            for(auto &path: paths)
            {
                int dx = x + path[0];
                int dy = y + path[1];
                if(isvalid(dx,dy,n,m) && !visited[dx][dy])
                {
                    visited[dx][dy] = true;
                    Q.push({dx,dy,d+1});
                    ans = max(ans,d+1);
                }
            }
        }
        
        return ans;
    }
};