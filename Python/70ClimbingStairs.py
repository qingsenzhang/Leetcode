class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs(n, {})
        
    def dfs(self, n, memo):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n in memo:
            return memo[n]
        
        memo[n] =  self.dfs(n - 1, memo) + self.dfs(n - 2, memo)
        return memo[n]
        
