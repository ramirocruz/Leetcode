class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj_list = {}
        ans = -1
        for idx, route in enumerate(routes):
            for node in route:
                if node not in adj_list:
                    adj_list[node] = []
                adj_list[node].append(idx)
        
        # print(adj_list)
        
        Q = deque()
        Q.append((source,0))
        seen_nodes = set({source})
        seen_routes = set()
        
        while Q:
            curr_node,time_taken = Q.popleft()
            if curr_node == target:
                ans = time_taken
            
            for bus_route in adj_list[curr_node]:
                if bus_route in seen_routes:
                    continue
                seen_routes.add(bus_route)
            
                for v in routes[bus_route]:
                    if v in seen_nodes:
                        continue
                    seen_nodes.add(v)
                    Q.append((v,time_taken + 1))
                
            
        return ans