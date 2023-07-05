#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    ans=[]
	    
	    def sub(i,sum):
	        if i==N:
	            ans.append(sum)
	            return
	        sub(i+1,sum+arr[i])
	        sub(i+1,sum)
	    sub(0,0)
	    ans.sort()
	    return ans
	    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends