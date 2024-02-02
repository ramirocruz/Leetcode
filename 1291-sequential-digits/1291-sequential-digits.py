class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def generate(n):
            num_list = []
            for start in range(1, 10 - n + 1):
                numstr = ""
                for i in range(start, start + n):
                    numstr += str(i)
                if numstr:    
                    num = int(numstr)
                    if num >= low and num <= high:
                        num_list.append(num)
            return num_list
        
        ans = []
        for num_len in range(len(str(low)),len(str(high)) + 1):
            temp = generate(num_len)
            # print(num_len, temp)
            ans.extend(temp)
        
        return sorted(ans)
                             
                             
                             