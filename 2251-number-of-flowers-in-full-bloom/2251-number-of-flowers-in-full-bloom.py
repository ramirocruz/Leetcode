
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        flower_sweep = {}
        
        for flower in flowers:
            
            if flower[0] not in flower_sweep:
                flower_sweep[flower[0]] = 1
            else:
                flower_sweep[flower[0]] += 1
                
            if flower[1] + 1 not in flower_sweep:
                flower_sweep[flower[1] + 1] = -1
            else:
                flower_sweep[flower[1] + 1] -= 1
        
        sorted_keys = sorted(flower_sweep.keys())
        # print(flower_sweep)
        # print(sorted_keys)
        people_list = [(idx,p) for idx,p in enumerate(people)]
        people_list.sort(key=lambda x: x[1])
        # print(people_list)
        n = len(sorted_keys)
        m = len(people_list)
        f_count = 0
        i,j = 0,0
        ans = [0]*m
        while i < n and j < m:
            if sorted_keys[i] <= people_list[j][1]:
                f_count += flower_sweep[sorted_keys[i]]
                i += 1
            else:
                ans[people_list[j][0]] = f_count
                j += 1
        
        while j < m:
            ans[people_list[j][0]] = f_count
            j += 1
        
        
        return ans
        