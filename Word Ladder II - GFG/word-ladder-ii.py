#User function Template for python3

class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        ans=[]
        q=[]
        q.append([beginWord])
        used=[]
        used.append(beginWord)
        level=0
        
        while q:
            seq = q.pop(0)
            if len(seq) > level:
                level +=1
                for it in used:
                    if it in wordset:
                        wordset.remove(it)
                
            word = seq[-1]
            if word == endWord:
                if len(ans) == 0:
                    ans.append(seq.copy())
                else:
                    if len(seq) == len(ans[0]):
                        ans.append(seq.copy())

            for i in range(len(word)):
                original = word[i]
                for j in range(97,123):
                    word =  word[:i] + chr(j) + word[i+1:]
                    if word in wordset:
                        seq.append(word)
                        q.append(seq.copy())
                        used.append(word)
                        seq.pop()
                    
                word = word[:i] + original + word[i+1:]   

        return ans


#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends