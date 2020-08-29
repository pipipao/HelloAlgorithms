# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        check=set()
        while head:
            check.add(head)
            head=head.next
            if head in check:
                return head
        return None