class Solution:
    def partitionString(self, s: str) -> int:
        vis=set()
        low=0
        ans=1
        
        for c in s:
            if c in vis:
                ans+=1
                vis=set()
            vis.add(c)
        return ans
            
        
        
                    
                