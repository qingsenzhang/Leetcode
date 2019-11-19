class Solution:
    def alienOrder(self, words: List[str]) -> str:
        ans = ""
        if not words:
            return ans
        
        mapping = {}
        degree = {}
        for word in words:
            for char in word:
                degree[char] = 0
                mapping[char] = set()
                
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in mapping[word1[j]]:
                        mapping[word1[j]].add(word2[j])
                        degree[word2[j]] += 1
                    break
                    
        dq = collections.deque([])
        for char in degree:
            if degree[char] == 0:
                dq.append(char)
        
        if not dq:
            return ans
        
        visited = set()
        while dq:
            char = dq.popleft()
            visited.add(char)
            ans += char
            for neighbor in mapping[char]:
                if neighbor not in visited:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 0:
                        dq.append(neighbor)
        if len(ans) != len(degree):
            return ""
        return ans        
