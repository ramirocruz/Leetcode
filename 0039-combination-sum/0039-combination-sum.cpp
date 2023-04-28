class Solution {
public:
    void helper(vector<int>&candidates, int target, vector<int> &tempdata, int tempsum, int pos,vector<vector<int>>&res)
    {
        if(tempsum > target)
            return;
        
        if(pos >= candidates.size())
        {
            if(tempsum == target)
                res.push_back(tempdata);
            return;
        }
        
        tempdata.push_back(candidates[pos]);
        helper(candidates,target,tempdata,tempsum + candidates[pos],pos,res);
        
        tempdata.pop_back();
        helper(candidates,target,tempdata,tempsum,pos + 1,res);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        vector<int>tempdata;
        vector<vector<int>>res;
        helper(candidates,target,tempdata,0,0,res);
        return res;
    }
};