class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter()
        for c in s:
            count[c] += 1
            
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
            
        return -1
