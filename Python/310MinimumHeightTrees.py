class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        
        indegree = {i : 0 for i in range(n)}
        neighbors = {i : set() for i in range(n)}
        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
            
        leaves = []
        for node in indegree:
            if indegree[node] == 1:
                leaves.append(node)
                
        unvisited = n
        while unvisited > 2:
            new_leaves = []
            for leaf in leaves:
                unvisited -= 1
                for neighbor in neighbors[leaf]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        new_leaves.append(neighbor)
            
            leaves = new_leaves
            
        return leaves
