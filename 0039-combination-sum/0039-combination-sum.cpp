class Solution {
public:
    void helper(vector<int>&candidates, int target, vector<int> &tempdata, int tempsum, int pos,set<vector<int>>&st,vector<vector<int>>&res)
    {
        if(tempsum > target)
            return;
        
        if(pos >= candidates.size())
        {
            if(st.count(tempdata) == 0)
            {
                st.insert(tempdata);
                if(tempsum == target)
                    res.push_back(tempdata);
                
            }
            return;
        }
        
        tempdata.push_back(candidates[pos]);
        helper(candidates,target,tempdata,tempsum + candidates[pos],pos,st,res);
        helper(candidates,target,tempdata,tempsum + candidates[pos],pos+1,st,res);
        
        tempdata.pop_back();
        helper(candidates,target,tempdata,tempsum,pos + 1,st,res);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        vector<int>tempdata;
        set<vector<int>>st;
        vector<vector<int>>res;
        sort(candidates.begin(),candidates.end());
        helper(candidates,target,tempdata,0,0,st,res);
        return res;
    }
};