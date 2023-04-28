class Solution {
public:
    void helper(vector<int>&temp,vector<vector<int>>&ans,int pos,vector<int>&nums)
    {
        if(pos == nums.size())
        {
            ans.push_back(temp);
            return;
        }
        
        temp.push_back(nums[pos]);
        helper(temp,ans,pos+1,nums);
        temp.pop_back();
        helper(temp,ans,pos+1,nums);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>temp;
        helper(temp,ans,0,nums);
        return ans;
    }
};