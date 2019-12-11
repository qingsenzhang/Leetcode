class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not logs or n == 0:
            return []
        
        ans = [0] * n
        stack = []
        prev = 0
        
        for log in logs:
            log = log.split(':')
            if log[1] == 'start':
                if stack:
                    ans[stack[-1]] += int(log[2]) - prev
                stack.append(int(log[0]))
                prev = int(log[2])
            else:
                ans[stack.pop()] += int(log[2]) - prev + 1
                prev = int(log[2]) + 1
            
        return ans
            
