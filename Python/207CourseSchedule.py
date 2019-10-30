class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or len(prerequisites) == 1:
            return True
        
        q = collections.deque([])
        indegrees = [0 for i in range(numCourses)]
        edges = {i : [] for i in range(numCourses)}
        
        for prereq in prerequisites:
            indegrees[prereq[0]] += 1
            edges[prereq[1]].append(prereq[0])
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                
        if not q:
            return False
        
        count = 0
        while q:
            course = q.popleft()
            count += 1
            for neighbor in edges[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
                    
        return count == numCourses
        
