# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head =  head.next
                
        dummy = ListNode(-1)
        prev = dummy
        
        while heap:
            curr = ListNode(heapq.heappop(heap))
            prev.next = curr
            prev = curr
            
        return dummy.next
        
