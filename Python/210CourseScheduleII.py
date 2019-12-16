class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegrees = {i : 0 for i in range(numCourses)}
        mapping = {i : set() for i in range(numCourses)}
        
        for prereq in prerequisites:
            mapping[prereq[1]].add(prereq[0])
            indegrees[prereq[0]] += 1
            
        dq = collections.deque([])
        for course in indegrees:
            if indegrees[course] == 0:
                dq.append(course)
                
        if not dq:
            return []
        
        ans = []
        while dq:
            course = dq.popleft()
            ans.append(course)
            for neighbor in mapping[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    dq.append(neighbor)
                    
        if len(ans) != numCourses:
            return []
        
        return ans
