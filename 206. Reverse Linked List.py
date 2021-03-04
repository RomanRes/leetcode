# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        while head:
            back, head = head, head.next
            back.next, result = result, back
        return result


# need Recursive
