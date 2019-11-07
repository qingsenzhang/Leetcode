class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s and not dict:
            return True
        elif not s or not dict:
            return False
            
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        
        for i in range(1, len(dp)):
            for word in wordDict:
                if i - len(word) >= 0 and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    
        return dp[-1]
