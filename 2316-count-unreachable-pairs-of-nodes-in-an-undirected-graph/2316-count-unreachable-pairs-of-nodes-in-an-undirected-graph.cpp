class Solution {
public:
    int dfs(int node, vector<vector<int>>&adj, vector<bool>&visited)
    {
        visited[node] = true;
        int ans = 1;
        for(auto v: adj[node])
        {
            if(visited[v] == false)
            {
                ans += dfs(v,adj,visited);
            }
        }
        return ans;
    }
    long long countPairs(int n, vector<vector<int>>& edges) {
        vector<vector<int>>adj(n);
        for(auto edge: edges)
        {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        vector<bool>visited(n,false);
        long long pairs_inside_comp = 0;
        long long total_pairs = ((long long) n * (n - 1))/2;
        for(int i = 0;i < n;i++)
        {
            if(visited[i] == false)
            {
                long long comp_len = dfs(i,adj,visited);
                pairs_inside_comp += (comp_len * (comp_len - 1))/2;
            }
        }
        
        // We will remove the count of pairs which are formed due to nodes of same component
        return total_pairs - pairs_inside_comp;
    }
};