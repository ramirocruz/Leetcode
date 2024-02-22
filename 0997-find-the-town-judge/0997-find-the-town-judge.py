class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = [0]*n
        outdeg = [0]*n
        for people in trust:
            u = people[0] - 1
            v = people[1] - 1
            indeg[v] += 1
            outdeg[u] += 1
        
        judge_count = 0
        judge = -1
        for i in range(n):
            if indeg[i] == n - 1 and outdeg[i] == 0:
                judge_count += 1
                judge = i + 1
        # print(judge_count, judge, indeg, outdeg)
        return judge if judge_count == 1 else -1