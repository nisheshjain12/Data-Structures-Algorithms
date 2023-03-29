class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n=len(satisfaction)
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        
        def rec(i,time):
            if i==n:
                return 0
            if dp[i][time] != -1:
                return dp[i][time]
            
            include = (time+1)*satisfaction[i] + rec(i+1,time+1)
            exclude = 0 + rec(i+1,time)
            dp[i][time] = max(include,exclude)
            return dp[i][time]
        
        satisfaction.sort()
        return rec(0,0) 