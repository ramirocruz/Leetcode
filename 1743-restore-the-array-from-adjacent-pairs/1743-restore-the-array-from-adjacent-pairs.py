class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        n = len(adjacentPairs) + 1
        g = {}
        ans = []
        indeg = {}
        for edge in adjacentPairs:
            u = edge[0]
            v = edge[1]
            if u not in g:
                g[u] = []
            if v not in g:
                g[v] = []
            if u not in indeg:
                indeg[u] = 0
            if v not in indeg:
                indeg[v] = 0
                
            g[u].append(v)
            g[v].append(u)
            
            indeg[u] += 1
            indeg[v] += 1
        
        # print(g)
        # print(indeg)
        roots = [node for node,l in indeg.items() if l == 1]
        # print(roots)
        visited = set()
        def dfs(node):
            visited.add(node)
            ans.append(node)
            
            for v in g[node]:
                if v not in visited:
                    dfs(v)
        
        dfs(roots[0])
        return ans