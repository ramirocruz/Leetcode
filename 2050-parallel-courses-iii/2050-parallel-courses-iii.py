from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        indegree = [0]*n
        graph = [[] for _ in range(n)]
        
        for relation in relations:
            graph[relation[0] - 1].append(relation[1] - 1)
            indegree[relation[1] - 1] += 1
        
        Q = deque()
        max_time = [0]*n
        for node in range(n):
            if indegree[node] == 0:
                Q.append(node)
                max_time[node] = time[node]
        
        while len(Q):
            node = Q.popleft()
            for v in graph[node]:
                max_time[v] = max(max_time[v],max_time[node] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    Q.append(v)
                    
        
        # print(graph,indegree,max_time)
        
        return max(max_time)
        
        return 0