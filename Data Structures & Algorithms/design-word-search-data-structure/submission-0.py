class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {} # a : TrieNode

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif char in cur.children:
                    cur = cur.children[char]
                elif char not in cur.children:
                    return False

            return cur.end
        return dfs(0, self.root)


