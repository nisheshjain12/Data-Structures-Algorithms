class Solution(object):
    def longestPalindromeSubseq(self, s):
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
            
        return rec(n-1,m-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        d = {}
        def f(s):
            if s not in d:
                maxL = 0    
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                d[s] = maxL
            return d[s]
        return f(s)  