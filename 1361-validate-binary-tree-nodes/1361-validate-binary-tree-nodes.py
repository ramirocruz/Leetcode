class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1]*n
        
        # Checking for duplicate parent
        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] == -1:
                    parent[leftChild[i]] = i
                else:
                    return False
            
            if rightChild[i] != -1:
                if parent[rightChild[i]] == -1:
                    parent[rightChild[i]] = i
                else:
                    return False
        
        # Checking for root
        
        root = None
        for i in range(n):
            if parent[i] == -1:
                if root == None:
                    root = i
                else:
                    return False # Duplicate root
        
        # No root
        if root == None:
            return False
        
        # Checking for cycle
        
        visited = [0]*n
        
        def dfs(node):
            
            visited[node] = 1
            
            result = True
            
            if leftChild[node] != -1:
                if visited[leftChild[node]] != 0:
                    return False
                
                result = result and dfs(leftChild[node])
            
            if rightChild[node] != -1:
                if visited[rightChild[node]] != 0:
                    return False
                
                result = result and dfs(rightChild[node])
            
            visited[node] = 2
            
            return result
        
        if dfs(root) == False:
            return False
        
        # Checking for connectivity
        
        if visited.count(0) > 0:
            return False
        
        return True
                
            
            