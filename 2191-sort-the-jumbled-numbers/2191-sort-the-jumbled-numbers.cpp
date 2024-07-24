class Solution {
public:
    
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        
        unordered_map<int,long long> mapped_nums;
        for(auto num : nums)
        {
            auto b_str = to_string(num);
            long long b_num = 0;
            for(auto c: b_str)
            {
                b_num += mapping[(c - '0')];
                b_num *= 10;
            }
            mapped_nums[num] = b_num;
        }
        sort(nums.begin(),nums.end(),[&mapped_nums](int a, int b){
            return mapped_nums[a] < mapped_nums[b];
        });
        return nums;
    }
};