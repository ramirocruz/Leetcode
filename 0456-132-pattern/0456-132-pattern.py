class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        curMin = int(1e9+7)
        mono_dec_stack = []
        # stores mono stack and a curmin in left till that number
        for elem in nums:
        
            while mono_dec_stack and mono_dec_stack[-1][0] <= elem:
                mono_dec_stack.pop()
           
            if mono_dec_stack and elem > mono_dec_stack[-1][1]:
                """
                    if stack is non empty that means there is a number greater that our cur elem
                    and since there is a left element smaller than current elem, that means we have 
                    found our triplet.
                    
                    minToLeft(mono_dec_stack[-1][1]) < elem < maxToLeft(mono_dec_stack[-1][0])
                """
                return True
                
            mono_dec_stack.append([elem,curMin])
            curMin = min(curMin,elem)
            
            
            
        return False
        