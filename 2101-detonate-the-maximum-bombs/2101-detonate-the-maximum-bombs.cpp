bool isInside(vector<int>&point, vector<int>&neighbour)
{
    long long dx = point[0] - neighbour[0];
    long long dy = point[1] - neighbour[1];
    long long r = point[2];
    return ((dx*dx + dy*dy) <= r*r);
}
int bfs(vector<int>&point, vector<vector<int>>&bombs)
{
    queue<vector<int>>Q;
    Q.push(point);
    map<vector<int>,int>detonated;
    for(auto bomb:bombs)
    {
        detonated[bomb]++;
    }
    detonated[point]--;
    int ans = 0;
    while(Q.size())
    {
        auto node = Q.front();
        Q.pop();
        ans++;
        for(int i=0;i < bombs.size();i++)
        {
            if(detonated[bombs[i]] > 0 && isInside(node,bombs[i]))
            {
                Q.push(bombs[i]);
                detonated[bombs[i]]--;
            }
        }
    }
 
    return ans;
}
class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        int ans = 0;
        
        for(int i=0;i<n;i++)
        {
            int cnt = 0;
            cnt = bfs(bombs[i], bombs);
            ans = max(ans,cnt);
        }
        
        return ans;
        
    }
};