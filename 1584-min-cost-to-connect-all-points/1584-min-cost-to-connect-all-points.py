class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
    
    def union_sets(self,x,y):
        parx = self.find_set(x)
        pary = self.find_set(y)
        
        if parx != pary:
            self.parent[pary] = parx
            return True
        
        return False
        
    def find_set(self,x):
        if x == self.parent[x]:
            return self.parent[x]
        self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]
    
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        edgeList = []
        for i in range(n):
            for j in range(i+1,n):
                edgelen = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                edge = (edgelen,i,j)
                edgeList.append(edge)

        
        edgeList.sort()
        
        # print(edgeList)
        
        dsu = DSU(n)
        cost = 0
        for edge in edgeList:
            if(dsu.union_sets(edge[1],edge[2]) == True):
                cost+= edge[0]
        
        # print(dsu.parent)
        return cost
            