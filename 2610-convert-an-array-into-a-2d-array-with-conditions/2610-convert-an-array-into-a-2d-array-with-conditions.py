class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 0
            num_count[num] += 1
        
        matrix_row_len = max(num_count.values())
        matrix = [[] for _ in range(matrix_row_len)]
        
        for key,val in num_count.items():
            for pos in range(val):
                matrix[pos].append(key)
        
        return matrix
            