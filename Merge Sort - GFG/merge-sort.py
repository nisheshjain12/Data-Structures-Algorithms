#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        temp=[]
        f=l
        s=m+1
        
        while f<=m and s<=r:
            if arr[f]<=arr[s]:
                temp.append(arr[f])
                f+=1
            else:
                temp.append(arr[s])
                s+=1
        
        while f<=m:
            temp.append(arr[f])
            f+=1
        while s<=r:
            temp.append(arr[s])
            s+=1
        for i in range(l,r+1):
            arr[i] = temp[i-l]
        return
        
        
    def mergeSort(self,arr, l, r):
        if l>=r:
            return 
        mid = (r+l)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends