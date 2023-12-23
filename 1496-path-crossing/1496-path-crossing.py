class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path_map = set({})
        x,y = 0,0
        path_map.add((x,y))
        for p in path:
            i,j = 0,0
            if p == 'N':
                i = 1
            elif p == 'S':
                i = -1
            elif p == 'E':
                j = 1
            else:
                j = -1
            
            x += i
            y += j
            if (x,y) in path_map:
                return True
            path_map.add((x,y))
        
        return False