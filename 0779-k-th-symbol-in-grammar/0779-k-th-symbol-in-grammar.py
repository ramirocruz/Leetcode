class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n: int, k: int, rootVal: int):
            if n == 1:
                return rootVal
            
            totalNodes = 2 ** (n - 1)
            
            if k > (totalNodes // 2): 
                # target is in right sub-tree of current root
                
                nextRootVal = 1 if rootVal == 0 else 0
                
                return dfs(n - 1, k - (totalNodes // 2), nextRootVal)
            
            else:
                
                nextRootVal = 0 if rootVal == 0 else 1
                return dfs(n - 1, k, nextRootVal)
        
        
        return dfs(n,k,0)