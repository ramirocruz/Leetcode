class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        """
        Assuming the list as a hashmap where index 1 to n can be used to store the respective elems.
        at 0 index the repeated element will lie
        """
        
        while nums[0] != nums[nums[0]]:
            nums[nums[0]],nums[0] = nums[0], nums[nums[0]]
        
        
        return nums[0]
        