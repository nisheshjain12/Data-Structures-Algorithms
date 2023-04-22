class Solution:
    def minInsertions(self, s: str) -> int:
        t1=s
        t2=s[::-1]
        n=len(t1)
        m=len(t2)
        dp=[[-1 for _ in range(m+1)]for _ in range(n+1)]
        
        def rec(i,j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if t1[i] == t2[j]:
                dp[i][j] =  1+rec(i-1,j-1)
                return dp[i][j]
            
            dp[i][j] = max(rec(i,j-1),rec(i-1,j))
            return dp[i][j]
            
        return len(s) - rec(n-1,m-1)