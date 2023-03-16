class Solution:
    def fib(self, n: int) -> int:
        # dp=[0 for _ in range(31)]
        # if n<=1:
        #     return n
        # if dp[n]>0:
        #     return dp[n]
        # dp[n] = fib(n-1) + fib(n-2)
        # return dp[n]   
        if n==0:
            return 0
        prev2=0
        prev=1
        for i in range(2,n+1):
            curr=prev+prev2
            prev2=prev
            prev=curr
        return prev

