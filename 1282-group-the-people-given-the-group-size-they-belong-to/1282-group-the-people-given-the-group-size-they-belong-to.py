class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        freq_dict = {}
        for idx,el in enumerate(groupSizes):
            if el in freq_dict:
                freq_dict[el].append(idx)
            else:
                freq_dict[el] = [idx]
        
        # print(freq_dict)
        ans = []
        for key,val in freq_dict.items():
            for i in range(0,len(val),key):
                ans.append(val[i:i+key])
                
        
        
        return ans
        
            
        
        
        