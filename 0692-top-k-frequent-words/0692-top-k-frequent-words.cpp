
bool comp(pair<int,string>&a,pair<int,string>&b)
{
    if(a.first == b.first)
        return a.second < b.second;
    return a.first > b.first;
}
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string,int>mp;
        
        for(auto word: words)
        {
            mp[word]++;
        }
        vector<pair<int,string>> temp;
        temp.reserve(mp.size());
        
        for(auto &p : mp)
        {
            temp.push_back({p.second,p.first});
        }
        
        sort(temp.begin(),temp.end(),comp);
        
        vector<string>ans(k);
        
        for(int i=0;i<k;i++)
        {
            ans[i] = temp[i].second;
        }
        
        
        return ans;
        
        
    }
};