class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        if(nums.size() <= 1) return nums;

        int i=0;
        int j=nums.size()-1;
        
        while(i<j) {
            if((nums[i]%2) == 1 && nums[j]%2 == 0) 
            {
                int swap = nums[i];
                nums[i] = nums[j];
                nums[j] = swap;
                i++;
                j--;
            }
            if(!(nums[i]%2)) i++;
            if(nums[j]%2) j--;
        }
        return nums;
    }
};