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
        
        for (auto &m : flower_sweep)
        {
            f_count += m.second;
            flower_sweep[m.first] = f_count;
        }
        
        vector<int>res;
        res.reserve(people.size());
        // for(auto &m : flower_sweep)
        // {
        //     cout << m.first << " "<<m.second << endl;
        // }
        for(auto &p : people)
        {
            auto pos = flower_sweep.lower_bound(p);
            
            int ans = 0;
            
            if(pos == flower_sweep.end())
                pos--;
            
            if((*pos).first > p)
            {
                if(pos == flower_sweep.begin())
                {
                    res.push_back(0);
                    continue;
                }
                else
                {
                    pos--;
                }
            }
            
            ans = (*pos).second;
            res.push_back(ans);
        }
        
        return res;
    }
};