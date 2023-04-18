class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''
        w1=0
        w2=0
        
        while w1<len(word1) and w2<len(word2):
            ans+=word1[w1]
            w1+=1
            ans+=word2[w2]
            w2+=1
        
        if w1<len(word1):
            for i in range(w1,len(word1)):
                ans+=word1[i]
        if w2<len(word2):
            for i in range(w2,len(word2)):
                ans+=word2[i]
        
        return ans