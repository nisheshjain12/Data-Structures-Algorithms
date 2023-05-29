#User function Template for python3

def Rearrange (arr,  n) : 
    
    for i in range(n):
        if arr[i]!=-1 and  arr[i]!=i:
            x = arr[i]
            
            while arr[x]!=-1 and arr[x] != x:
                y=arr[x]
                arr[x] = x
                x=y
            arr[x]  = x
            if arr[i] !=i:
                arr[i] = -1
            
    return arr
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Rearrange(arr, n);
    print(*res)




# } Driver Code Ends