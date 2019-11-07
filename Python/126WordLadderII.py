class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        wordList.add(beginWord)
        length = {}
        
        self.bfs(endWord, beginWord, wordList, length)
        
        ans = []
        self.dfs(beginWord, endWord, length, wordList, [beginWord], ans)
        return ans

    def bfs(self, start, end, dict, length):
        length[start] = 0
        dq = collections.deque([start])
        while dq:
            word = dq.popleft()
            for w in self.getNextWord(word, dict):
                if w not in length:
                    length[w] = length[word] + 1
                    dq.append(w)
            
    def getNextWord(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char != word[i] and left + char + right in dict:
                    words.append(left + char + right)
        return words
        
    def dfs(self, curr, target, length, dict, path, ans):
        if curr == target:
            ans.append(path.copy())
            return 
        
        for word in self.getNextWord(curr, dict):
            if length[word] == length[curr] - 1:
                path.append(word)
                self.dfs(word, target, length, dict, path, ans)
                path.pop()
