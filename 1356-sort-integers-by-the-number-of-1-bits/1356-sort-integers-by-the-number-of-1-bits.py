class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def get_one_count(elem):
            fcount = 0
            for i in range(32):
                if (elem&(1 << i)):
                    fcount += 1
                    
            return (fcount,elem)
        
        arr.sort(key=get_one_count)
        
        return arr
        