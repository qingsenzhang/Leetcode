class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True
        
        n = len(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < n and not s[left].isalpha() and not s[left].isdigit():
                left += 1
            while right >= 0 and not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            
            if left <= right:
                if not s[left].lower() == s[right].lower():
                    return False
                left += 1
                right -= 1
                
        return True
        
