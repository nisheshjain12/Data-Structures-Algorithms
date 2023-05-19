#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, summ):
        dp = [[-1 for i in range(summ+1)] for _ in range(N+1)]
        
        def rec(i,target):
            if target == 0:
                return True
            if i==0:
                return arr[i] == target
            
            if dp[i][target] != -1:
                return dp[i][target]
                
            nottake = rec(i-1,target)
            take = False
            if arr[i] <= target:
                take = rec(i-1,target-arr[i])
            
            dp[i][target] = take or nottake
            return dp[i][target]
        return rec(N-1,summ)

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