class Solution {
public:
    void helper(vector<vector<int>>&ans,vector<int>&temp,int pos ,vector<int>&nums,set<vector<int>> &st)
    {
        if(pos == nums.size())
        {
            if(st.count(temp) == 0)
            {
                ans.push_back(temp);
                st.insert(temp);
            }
            
            return;
        }
        temp.push_back(nums[pos]);
        helper(ans,temp,pos+1,nums,st);
        temp.pop_back();
        helper(ans,temp,pos+1,nums,st);
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        set<vector<int>> st;
        vector<vector<int>>ans;
        vector<int>temp;
        helper(ans,temp,0,nums,st);
        return ans;
    }
};