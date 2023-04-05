class Solution:
    def isValid(self, s: str) -> bool:
        q=[]
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                q.append(s[i])
            elif s[i] == ')' and len(q)!=0 and q[len(q)-1] == '(':
                q.pop()
            elif s[i] == ']' and len(q)!=0 and q[len(q)-1] == '[':
                q.pop()
            elif s[i] == '}' and len(q)!=0 and q[len(q)-1] == '{':
                q.pop()
            else:
                return False
                
        if len(q)==0:
            return True
        return False
                
                