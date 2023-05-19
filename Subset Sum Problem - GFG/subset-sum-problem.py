#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, summ):
        dp = [[False for i in range(summ+1)] for _ in range(N+1)]
        
        for i in range(N):
            dp[i][0] = True
        if arr[0] <= summ:
            dp[0][arr[0]] = True
        
        for i in range(1,N):
            for j in range(1,summ+1):
                nottake = dp[i-1][j]
                take = False
                if arr[i] <= j:
                    take = dp[i-1][j-arr[i]]
                dp[i][j] = take or nottake
        return dp[N-1][summ]
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends