class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [ [[-1]*(len(s3)+1) for _ in range(len(s2)+1) ]for _ in range(len(s1)+1)]
        
        def longest_subsequence_helper(i,j,k):
            if(i == len(s1) and j == len(s2) and k == len(s3)):
                return True
            if(dp[i][j][k] != -1):
                return dp[i][j][k]
            
            if(i < len(s1) and j < len(s2) and s1[i] == s3[k] and s2[j] == s3[k]):
                dp[i][j][k] =  longest_subsequence_helper(i+1,j,k+1) or longest_subsequence_helper(i,j+1,k+1)
                return dp[i][j][k]
            
            if(i < len(s1) and s1[i] == s3[k]):
                dp[i][j][k] =  longest_subsequence_helper(i+1,j,k+1)
                return dp[i][j][k]
            
            if(j < len(s2) and s2[j] == s3[k]):
                dp[i][j][k] = longest_subsequence_helper(i,j+1,k+1)
                return dp[i][j][k]
            
            dp[i][j][k] = False
            return dp[i][j][k]
        
        if(len(s1) + len(s2) != len(s3)):
            return False
        
        
        # print(len(dp),len(dp[0]),len(dp[0][0]))
        return longest_subsequence_helper(0,0,0)
            
        