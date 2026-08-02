class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            i = ord(ch) - ord('a')

            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]

        cur.end = True
        
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # Correctly iterate through valid instantiated child nodes in the list
                    for child in cur.children:
                        if child is not None:
                            if dfs(i + 1, child):
                                return True
                    return False
                else:
                    # Correctly calculate the alphabetical index for character lookup
                    idx = ord(c) - ord('a')
                    if cur.children[idx] is None:
                        return False
                    cur = cur.children[idx]
            return cur.end

        return dfs(0, self.root)