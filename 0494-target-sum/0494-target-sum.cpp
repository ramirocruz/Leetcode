class Solution {
public:
    int helper(vector<int>&nums,int target,int pos, vector<int>&tempdata,int tempsum)
    {
        if(pos == nums.size())
        {
            if(tempsum == target)
            {
                return 1;
            }

            return 0;
        }
        
        int count = 0;
        // nums[pos] is added to the sum
        tempdata.push_back(nums[pos]);
        count += helper(nums,target,pos+1,tempdata,tempsum + nums[pos]);
        
        // nums[pos] is substracted from the sum
        tempdata.pop_back();
        count += helper(nums,target,pos+1,tempdata,tempsum - nums[pos]);
        
        return count;
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        
        vector<int>tempdata;
        return helper(nums,target,0,tempdata,0);
    }
};