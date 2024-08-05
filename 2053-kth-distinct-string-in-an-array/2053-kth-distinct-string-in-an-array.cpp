class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        vector<string>distinct_str;
        // distinct_str.resize(arr.size());
        unordered_map<string, int> mp;
        for(auto &x : arr)
        {
            mp[x]++;
        }
        // cout << mp.size() << endl;
        if(mp.size() < k)
            return "";
        for(auto &x : arr)
        {
            if (mp[x] == 1){
                distinct_str.push_back(x);
            }
        }
        // cout << distinct_str.size() << endl;
        // for(auto x : distinct_str)
        //     cout << x <<" ";
        // cout << endl;
        if(distinct_str.size() < k)
            return "";
        return distinct_str[k-1];
    }
};