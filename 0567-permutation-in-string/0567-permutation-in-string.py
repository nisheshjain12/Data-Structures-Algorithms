class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        alpha=[0 for _ in range(26)]
        
        for i in range(n):
            alpha[ord(s1[i])-ord('a')]+=1
        
        if len(s1)>len(s2):
            return False
        l=0
        r=n-1
        
        def valid(l,r,temp):
            for i in range(l,r+1):
                temp[ord(s2[i])  - ord('a')]-=1
                
            if min(temp)==0 and max(temp)==0:
                return True
            return False    
            
        while r<len(s2):
            temp=alpha.copy()
            if valid(l,r,temp):
                return True
            l+=1
            r+=1
            
        return False
            

