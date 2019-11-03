"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        m = {}
        h = Node(head.val, None, None)
        m[head] = h

        p = head
        q = h

        while p != None:
        	q.random = p.random
        	if p.next != None:
        		q.next = Node(p.next.val, None, None)
        		m[p.next] = q.next
        	else: 
        		q.next = None
        	p = p.next
        	q = q.next

        p = h
        while p != None:
        	if p.random != None:
        		p.random = m[p.random]
        	p = p.next
        return h
