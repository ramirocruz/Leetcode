class Solution {
public:
    
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        
        sort(nums.begin(),nums.end(),[&mapping](int a, int b){
            auto a_str = to_string(a);
            auto b_str = to_string(b);
            long long a_num = 0;
            long long b_num = 0;
            for(auto c: a_str)
            {
                a_num += mapping[(c - '0')];
                a_num *= 10;
            }
            for(auto c: b_str)
            {
                b_num += mapping[(c - '0')];
                b_num *= 10;
            }
            return a_num < b_num;
        });
        return nums;
    }
};