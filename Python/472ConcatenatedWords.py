class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and suffix in words:
                    return True
                elif prefix in words and dfs(suffix):
                    return True
                elif suffix in words and dfs(prefix):
                    return True
                
            return False
                
        ans = []
        for word in words:
            if dfs(word):
                ans.append(word)
                
        return ans
