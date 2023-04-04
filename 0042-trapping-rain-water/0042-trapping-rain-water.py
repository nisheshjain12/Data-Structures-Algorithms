class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        pre=[0]*n
        post=[0]*n
        
        for i in range(n):
            if i==0:
                pre[i] = height[0]
            else:
                pre[i] = max(height[i],pre[i-1])
            
            
        for i in range(n-1,-1,-1):
            if i==n-1:
                post[i] = height[n-1]
            else:
                post[i] = max(height[i],post[i+1])
        
        ans=0
        for i in range(n):
            water = min(pre[i],post[i]) - height[i]
            ans+=max(0,water)
        return ans
            