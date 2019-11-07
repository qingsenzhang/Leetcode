class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or \
                       self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, s, start, end):
        if start == end:
            return True
        
        while start < end and s[start] == s[end]:
            start += 1 
            end -= 1
            
        return start >= end
