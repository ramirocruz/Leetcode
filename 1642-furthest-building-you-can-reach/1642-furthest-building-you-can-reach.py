class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        minheap = []
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                """
                 We are storing the records of all the differences
                 And we want to use the ladders for the top 3 differences
                 and bricks for the rest
                 That's why whenever we encounter any bigger diff we will discard
                 the smallest diff and use bricks for that.
                 
                """
                heappush(minheap, diff)
                ladders -= 1
                if ladders < 0: # We have filled the diff more than the no. of ladders
                    # We are discarding the smallest diff to be filled by bricks
                    exchange_element = heappop(minheap)
                    bricks -= exchange_element
                
                if bricks < 0:
                    return i
        return n - 1
            