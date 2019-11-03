class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or len(s) == 0 or k == 0:
            return 0
        
        if len(s) < k:
            return len(s)
        
        left, right, distinct = 0, 1, 1
        current_set = {s[0] : 0}
        max_len = 1
        
        while right < len(s):
            if s[right] in current_set:
                current_set[s[right]] = right
            else:
                if len(current_set) == k:
                    min_idx = min(current_set.values())
                    while left <= min_idx:
                        left += 1
                    del current_set[s[min_idx]]
                current_set[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
