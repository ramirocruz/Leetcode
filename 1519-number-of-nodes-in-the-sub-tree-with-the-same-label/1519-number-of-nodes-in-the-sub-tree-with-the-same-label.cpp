class Solution {
public:
    array<int,26> dfs(int node,vector<vector<int>>&g,string &labels,vector<bool>&vis,vector<int>&count)
    {
        vis[node] = true;
        array<int,26>fcount;
        fcount.fill(0);
        fcount[labels[node] - 'a']++;
        
        for(auto &u : g[node])
        {
            if(vis[u])
                continue;
            
            auto tempcnt = dfs(u,g,labels,vis,count);
            for(int i=0;i<26;i++)
            {
                fcount[i] += tempcnt[i];
            }
        }
        
        
        count[node] = fcount[labels[node] - 'a'];
        
        return fcount;        
    }
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        
        vector<int>ans(n);
        vector<vector<int>>g(n);
        vector<bool>vis(n);
        
        for(auto &p : edges)
        {
            g[p[0]].push_back(p[1]);
            g[p[1]].push_back(p[0]);
        }
        
        dfs(0,g,labels,vis,ans);
        
        
        return ans;
    }
};