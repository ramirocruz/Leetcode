class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        
        unordered_map<int,int>fcount;
        for(auto &x:tasks)
            fcount[x]++;
        
        int ans = 0;
        
        for(auto &p : fcount)
        {
            
            int cnt = p.second;
            
            if(cnt == 1)
                return -1;
            
            if(cnt % 3 == 0)
                ans += cnt/3;
            else if(cnt % 3 == 1)
            {
                ans += (cnt - 3)/3 + 2;
                // We will not divide the remaining 4 with 3 but with 2 itself
            }
            else if(cnt % 3 == 2)
            {
                ans += cnt/3 + 1;
                // Since we are left with the 2 we will divide it by 2
            }
            
                
        }
        
        
        return ans;
    }
};