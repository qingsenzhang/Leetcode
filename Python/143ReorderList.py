# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        first_half = []
        second_half = []
        curr = head
        i = 0
        while curr:
            i += 1
            curr = curr.next
        
        mid = (i + 1) // 2
        curr = head
        for i in range(mid):
            first_half.append(curr)
            curr = curr.next
            
        while curr:
            second_half.append(curr)
            curr = curr.next
            
        i = 0
        while i < mid - 1 and second_half:
            first_half[i].next = second_half.pop()
            first_half[i].next.next = first_half[i+1]
            i += 1
            
        if second_half:
            first_half[-1].next = second_half.pop()
            first_half[-1].next.next = None
        else:
            first_half[-1].next = None
            
        return head
            
            
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow
        mid.next = self.reverseList(mid.next)
        
        curr = mid.next
        print(mid.val)
        while curr:
            print(curr.val)
            curr = curr.next
        
        curr = head
        toAdd = mid.next
        while curr != mid and toAdd:
            tmp = toAdd.next
            toAdd.next = curr.next
            curr.next = toAdd
            curr = curr.next.next
            toAdd = tmp
        
        if toAdd:
            curr.next = toAdd
            toAdd.next = None
        else:
            curr.next = None
        
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return prev
                   
            
            
            
            
        
