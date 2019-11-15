class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if not s or len(s) < len(p):
            return ans
        
        count_p = collections.Counter(p)
        count_s = collections.Counter(s[:len(p) - 1])
        matched = True
        
        for i in range(len(p) - 1, len(s)):
            matched = True
            count_s[s[i]] += 1
                
            if count_p == count_s:
                ans.append(i - len(p) + 1)
                
            count_s[s[i - len(p) + 1]] -= 1
            if count_s[s[i - len(p) + 1]] == 0:
                del count_s[s[i - len(p) + 1]]
                    
        return ans
