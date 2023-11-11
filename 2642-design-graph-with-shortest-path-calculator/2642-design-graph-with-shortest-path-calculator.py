class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        self.n = n
        for u,v,cost in edges:
            self.graph[u].append((v,cost))

    def addEdge(self, edge: List[int]) -> None:
        u,v,cost = edge
        self.graph[u].append((v,cost))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        min_heap = [(0,node1)]
        cost_list = [inf]*self.n
        cost_list[node1] = 0
        while min_heap:
            curr_cost, curr_node = heappop(min_heap)
            if cost_list[curr_node] < curr_cost:
                continue
            if curr_node == node2:
                return curr_cost
            
            for v,cost in self.graph[curr_node]:
                new_cost = curr_cost + cost
                if new_cost < cost_list[v]:
                    cost_list[v] = new_cost
                    heappush(min_heap,(new_cost,v))
        
        return -1
            


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)