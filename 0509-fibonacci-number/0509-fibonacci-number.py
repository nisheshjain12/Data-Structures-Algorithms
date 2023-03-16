class Solution:
    def fib(self, n: int) -> int:
        dp=[0 for _ in range(31)]
        def fibb(n):
            if n<=1:
                return n
            if dp[n]>0:
                return dp[n]
            dp[n] = fibb(n-1) + fibb(n-2)
            return dp[n]   
        return fibb(n)
        

