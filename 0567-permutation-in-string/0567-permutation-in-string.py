class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        alpha=[0 for _ in range(26)]
        beta=[0 for _ in range(26)]
        
        if n>m:
            return False
        
        def compare(a,b):
            for i in range(26):
                if a[i]!=b[i]:
                    return False
            return True
        
        for i in range(n):
            alpha[ord(s1[i])-ord('a')]+=1
        
        for i in range(n):
            beta[ord(s2[i])-ord('a')]+=1
        
        if compare(alpha,beta):
            return True
        
        for i in range(n,m):
            beta[ord(s2[i-n])-ord('a') ]-=1
            beta[ord(s2[i])-ord('a') ]+=1
        
            if compare(alpha,beta):
                return True
            
        return False
            

