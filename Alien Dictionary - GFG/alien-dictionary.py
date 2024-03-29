#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):
        
        def cycle(adj):
            n=len(adj)
            vis=[False for _ in range(n)]
            indegree = [0 for _ in range(n)]
            for i in range(n):
                for it in adj[i]:
                    indegree[it] += 1
            q=[]
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
            ans = []
            
            while(len(q) != 0):
                node = q.pop(0)
                ans.append(node)
                for child in adj[node]:
                    indegree[child]-=1
                    if indegree[child] == 0 :
                        q.append(child)
            return ans
                
        adj = [[] for _ in range(K)]
        for i in range(N-1):
            s1=alien_dict[i]
            s2=alien_dict[i+1]
            
            for p in range(min(len(s1),len(s2))):
                if s1[p] != s2[p]:
                    adj[ord(s1[p]) - ord('a')].append(ord(s2[p]) - ord('a'))
                    break
        
        ans = cycle(adj)
        string = ""
        for a in ans:
            string+= chr(a + ord('a'))
        return string
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends