class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root
            for j in range(i, len(word)):
                c = word[j]
                if c != '.':
                    if c not in curr.children:
                        return False

                    curr = curr.children[c]

                else:
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                        
                    return False

            return curr.endOfWord

        return dfs(0, self.root)