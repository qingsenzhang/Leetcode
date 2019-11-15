"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
            
        cloned_root = Node(node.val, [])
        dq = collections.deque([node])
        mapping = {node : cloned_root}
        while dq:
            node = dq.popleft()
            for neighbor in node.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val, [])
                    mapping[node].neighbors.append(mapping[neighbor])
                    dq.append(neighbor)
                else:
                    mapping[node].neighbors.append(mapping[neighbor])
                    
        return cloned_root
