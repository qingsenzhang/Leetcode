class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {char : None for char in 'abcdefghijklmnopqrstuvwxyz'}
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for char in word:
            if not curr.children[char]:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(word, self.root)
        
    def dfs(self, word, node):
        if not node:
            return False
        
        if word == "":
            return node.isWord
        
        if word[0] != '.':
            if node.children[word[0]]:
                return self.dfs(word[1:], node.children[word[0]])
            else:
                return False
        else:
            for key in node.children:
                if self.dfs(word[1:], node.children[key]):
                    return True
                
            return False
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
