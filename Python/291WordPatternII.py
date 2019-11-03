class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        if not pattern and not str:
            return True
        
        if not pattern or len(pattern) == 0 or len(str) == 0:
            return False
            
        return self.dfs(pattern, str, {}, set())
        
    def dfs(self, pattern, str, mapping, used):
        if len(pattern) == 0 and len(str) == 0:
            return True
        if len(pattern) != 0 and len(str) == 0:
            return False
        if len(pattern) == 0 and len(str) != 0:
            return False
        
        char = pattern[0]
        if char in mapping:
            if len(mapping[char]) > len(str):
                return False
            else:
                if mapping[char] == str[:len(mapping[char])]:
                    return self.dfs(pattern[1:], str[len(mapping[char]):], mapping, used)
                else:
                    return False
            
        for i in range(1, len(str) + 1):
            if str[:i] in used:
                continue
            mapping[char] = str[:i]
            used.add(str[:i])
            if self.dfs(pattern[1:], str[i:], mapping, used):
                return True
            del mapping[char]
            used.remove(str[:i])
            
        return False
