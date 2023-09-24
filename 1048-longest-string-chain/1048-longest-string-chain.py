class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordlist = {}
        
        for word in words:
            if len(word) not in wordlist:
                wordlist[len(word)]= [word]
            else:
                wordlist[len(word)].append(word)
        
        # print(wordlist)
        
        lenkeys = list(wordlist.keys())
        lenkeys.sort()
        graph = {}
        
        visited = {}
        
        def appendGraph(keylen):
            for word in wordlist[keylen]:
                graph[word] = []
                for suc_word in wordlist[keylen+1]:
                    graph[word].append(suc_word)
 
        for i in range(len(lenkeys) - 1):
            if(lenkeys[i] + 1 == lenkeys[i+1]):
                appendGraph(lenkeys[i])
        
        def isSubsequence(word1,word2):
            i,j = 0,0
            while i < len(word1) and j < len(word2):
                if(word1[i] == word2[j]):
                    i += 1
                j += 1
            
            if(i == len(word1)):
                return True
            return False
        dp = {}
        def dfs(word):
            if word in dp:
                return dp[word]
            if word not in graph:
                return 1
            maxlen = 0
            for w in graph[word]:
                if(isSubsequence(word,w)):
                    maxlen = max(maxlen,dfs(w))
            
            dp[word] = maxlen + 1
            return dp[word]
        
        ans = 0

        for key in lenkeys[::-1]:
            for word in wordlist[key]:                
                ans = max(ans,dfs(word))
                
        
        # print(graph)
        # print(lenkeys)
        return ans