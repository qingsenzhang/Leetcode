class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if len(graph) == 1 and not graph[0]:
            return True
        
        visited = set()
        graph = {i : graph[i] for i in range(len(graph))}
        for node in graph:
            if node in visited:
                continue

            color = {node: 1}
            dq = collections.deque([node])
            while dq:
                node = dq.popleft()
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = -color[node]
                        visited.add(neighbor)
                        dq.append(neighbor)
                    else:
                        if color[node] == color[neighbor]:
                            return False
                        
        return True
