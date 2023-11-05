class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        Q = deque(arr[1:])
        curr = arr[0]
        max_element = max(arr)
        winstreak = 0
        
        while Q:
            opponent = Q.popleft()
            if curr > opponent:
                Q.append(opponent)
                winstreak += 1
            else:
                Q.append(curr)
                curr = opponent
                winstreak = 1
            
            if winstreak == k or curr == max_element:
                return curr
        
        