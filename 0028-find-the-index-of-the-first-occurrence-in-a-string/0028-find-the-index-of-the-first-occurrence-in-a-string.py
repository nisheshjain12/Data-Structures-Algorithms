class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        
        hey=0
        ney=0
        
        while hey<n:
            if haystack[hey] == needle[ney]:
                temp=hey
                while temp<n and ney<m and haystack[temp] == needle[ney]:
                    temp+=1
                    ney+=1
                if ney==m:
                    return hey
                else:
                    ney=0
            hey+=1
                     
        return -1