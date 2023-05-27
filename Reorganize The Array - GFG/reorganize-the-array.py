#User function Template for python3

def Rearrange (arr,  n) : 
    ans=[-1 for _ in range(n)]
    for i in range(n):
        if arr[i]!=-1:
            ans[arr[i]] = arr[i]
    return ans
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Rearrange(arr, n);
    print(*res)




# } Driver Code Ends