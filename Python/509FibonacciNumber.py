class Solution:
    def fib(self, N: int) -> int:
        return self.dfs(N, {0:0, 1:1})
        
    def dfs(self, N, cache):
        if N in cache:
            return cache[N]
    
        else:
            ans = self.dfs(N - 2, cache) + self.dfs(N - 1, cache)
            cache[N] = ans
            return ans
