class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        i = 0
        prev = 0
        while i < len(arr):
            if arr[i] - prev > 1:
                arr[i] = prev + 1
                
            prev = arr[i]
            i += 1
        
        return arr[-1]