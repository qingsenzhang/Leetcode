class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        for i in range(len(s)):
            if s[i] != "0":
                dp[i+1] += dp[i]
            if i - 1 >= 0:
                num = int(s[i - 1]) * 10 + int(s[i])
                if 10 <= num <= 26:
                    dp[i+1] += dp[i-1]
        
        return dp[len(s)]
