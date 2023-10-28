class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        g = {}
        g['a'] = ['e']
        g['e'] = ['a','i']
        g['i'] = ['a','e','o','u']
        g['o'] = ['i','u']
        g['u'] = ['a']
        
        vowels = ['a','e','i','o','u']
        MOD = int(1e9 + 7)
        
        @cache
        def dfs(node, chain_len):
            if chain_len == n:
                return 1
            
            res = 0
            for v_node in g[node]:
                res = (res + dfs(v_node,chain_len + 1))%MOD
            
            return res
        
        ans = 0
        
        for v in vowels:
            ans = (ans + dfs(v,1))%MOD
            
        
        return ans