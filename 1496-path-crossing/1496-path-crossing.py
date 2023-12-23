class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path_map = set({})
        x,y = 0,0
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }
        path_map.add((x,y))
        for p in path:
            dx, dy = moves[p]
            x += dx
            y += dy
            if (x,y) in path_map:
                return True
            path_map.add((x,y))
        
        return False