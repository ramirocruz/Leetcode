bool isvalid(int i,int j,int n,int m)
{
    if(i < 0 || j < 0 || i >=n || j >= m)
        return false;
    return true;
}
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        
        queue<array<int,3>> Q;
        int n = mat.size();
        int m = mat[0].size();
        vector<vector<int>> resmat(n, vector<int>(m,INT_MAX));
        for(int i=0;i < n;i++)
        {
            for(int j=0;j < m;j++)
            {
                if(mat[i][j] == 0)
                {
                    resmat[i][j] = 0;
                    Q.push({i,j,0});
                }
            }
        }
        int paths[4][2] = {{-1,0},{1,0},{0, 1}, {0, -1}};
        while(Q.size())
        {
            auto f = Q.front();
            int x = f[0];
            int y = f[1];
            int d = f[2];
            Q.pop();
            for(auto &path: paths)
            {
                int dx = x + path[0];
                int dy = y + path[1];
                if(isvalid(dx,dy,n,m) && resmat[dx][dy] > d + 1)
                {
                    Q.push({dx,dy,d+1});
                    resmat[dx][dy] = d + 1;
                }
            }
        }
        return resmat;
    }
};