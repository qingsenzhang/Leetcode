class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
