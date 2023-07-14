class Solution:
    def dfs_cycle(self,node,vis,adj):
        vis[node] = 1
        
        for neighbour in adj[node]:
            if(vis[neighbour] == 1):
                return True
            if(vis[neighbour] == 0 and self.dfs_cycle(neighbour,vis,adj)):
                return True
        
        vis[node] = 2
        return False
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        vis = [0]*numCourses
        for p in prerequisites:
            adj[p[1]].append(p[0])
        
        for i in range(numCourses):
            if(self.dfs_cycle(i,vis,adj)):
                return False
        
        return True
        