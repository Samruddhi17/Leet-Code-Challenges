# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast =head
        
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow: 
                while (slow!=head): #fast is l+k steps ahead of slow
                    slow = slow.next  #k steps
                    head = head.next  #1 loop 
                return slow
        return None