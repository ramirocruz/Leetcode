class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = {}
        src = "JFK"
        for edge in tickets:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
        

        for node in graph:
            graph[node].sort(reverse=True)
            
        stk = [src]
        result = []
        
        while len(stk):
            node = stk[-1]
            
            if(node not in graph or len(graph[node]) == 0):
                result.append(node)
                stk.pop()
            else:
                u = graph[node][-1]
                stk.append(u)
                graph[node].pop()
        
            
        return result[::-1]
        