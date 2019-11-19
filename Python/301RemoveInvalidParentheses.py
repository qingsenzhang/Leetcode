class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = set()
        dq = collections.deque([s])
        visited = set([s])
            
        while dq:
            found = False
            for i in range(len(dq)):
                word = dq.popleft()
                if self.isValid(word):
                    found = True
                    ans.add(word)
                elif not found:
                    for i in range(len(word)):
                        if word[i] != '(' and word[i] != ')':
                            continue
                        else:
                            new_word = word[:i] + word[i+1:]
                            if new_word not in visited:
                                visited.add(new_word)
                                dq.append(new_word)
            if found:
                break
        return list(ans)   
            
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = 0
        for char in s:
            if char == '(':
                stack += 1
            elif char == ')':
                if stack == 0:
                    return False
                else:
                    stack -= 1
        return stack == 0
