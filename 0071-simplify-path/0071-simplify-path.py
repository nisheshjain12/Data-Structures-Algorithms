class Solution:
    def simplifyPath(self, path: str) -> str:
        q=[]
        curr=''
        for c in path + '/':
            if c=="/":
                if curr == '..':
                    if q:
                        q.pop()
                elif curr!='' and curr!= '.':
                    q.append(curr)
                curr=''       
            else:
                curr+=c
            
        return '/'+'/'.join(q)
                