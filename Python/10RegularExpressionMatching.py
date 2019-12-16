class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        ls, lp = len(s), len(p)
        dp = [[False] * (lp + 1) for i in range(ls + 1)]
        dp[0][0] = True
        for i in range(2, lp + 1):
            if p[i-1] == '*' and dp[0][i-2]:
                dp[0][i] = True
                
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] != '.' and p[j-2] != s[i-1]:
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
        
        return dp[-1][-1]
