class Solution:
    def dfs_cycle(self,node,adj,visit):
        visit[node] = 1
        for neighbour in adj[node]:
            if(visit[neighbour] == 1):
                return True
            if(visit[neighbour] == 0):
                if(self.dfs_cycle(neighbour,adj,visit)):
                    return True
        
        visit[node] = 2
        return False
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)
        
        visit = [0]*n
        
        for i in range(n):
            if(visit[i] == 0):
                self.dfs_cycle(i,adj,visit)
        
        safeNodes = []
        for i in range(n):
            if(visit[i] == 2):
                safeNodes.append(i)
        return safeNodes
        