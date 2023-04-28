class Solution {
public:
    int helper(vector<int>&nums,int target,int pos,int tempsum)
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
        count += helper(nums,target,pos+1,tempsum + nums[pos]);
        
        // nums[pos] is substracted from the sum
        count += helper(nums,target,pos+1,tempsum - nums[pos]);
        
        return count;
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        return helper(nums,target,0,0);
    }
};