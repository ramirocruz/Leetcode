
int reverse_lb(vector<pair<int,int>>&v,int target)
{
    int l = 0;
    int r = v.size() - 1;
    int ans = -1;
    while(l <= r)
    {
        int mid = (l + r)/2;
        
        if(v[mid].first <= target)
        {
            ans = mid;
            l = mid + 1;
        }
        else
        {
            r = mid - 1;
        }
    }
    
    return ans;
}
class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        
        map<int,int>flower_sweep;
        for (auto &flower:flowers)
        {
            flower_sweep[flower[0]]++;
            flower_sweep[flower[1] + 1]--;
        }
        
        int f_count = 0;
        
        vector<pair<int,int>>v;
        
        for (auto &m : flower_sweep)
        {
            f_count += m.second;
           v.push_back({m.first,f_count});
        }
        
        
        vector<int>res;
        for(auto &p : people)
        {
            int pos = reverse_lb(v,p);
            if(pos == -1)
            {
                res.push_back(0);
            }
            else
            {
                res.push_back(v[pos].second);
            }
        }
        
        return res;
    }
};