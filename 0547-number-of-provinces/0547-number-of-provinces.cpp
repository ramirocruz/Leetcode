class Solution {
public:
    void dfs(int node, vector<vector<int>>&g, vector<bool>&visited)
    {
        visited[node] = true;
        for(int v = 0; v < g.size(); v++)
        {
            if(g[node][v] && visited[v] == false)
            {
                dfs(v,g,visited);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool>visited(n,false);
        int ans = 0;
        for(int i=0;i<n;i++)
        {
            if(visited[i] == false)
            {
                dfs(i,isConnected,visited);
                ans++;
            }
        }
        
        return ans;
    }
};