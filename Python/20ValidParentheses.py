class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        elif len(s) == 1:
            return False
        
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if char == ')':
                    if stack[-1] != '(':
                        return False
                elif char == ']':
                    if stack[-1] != '[':
                        return False
                else:
                    if stack[-1] != '{':
                        return False
                stack.pop()
                
        return not stack
                    
                    
        
