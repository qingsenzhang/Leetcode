class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        if not words:
            return ""
        print(words)
        return " ".join(words[::-1])
        
