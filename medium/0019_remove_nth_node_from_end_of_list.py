"""Given the head of a linked list, remove the nth node 
from the end of the list and return its head."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        i = 1
        current = head
        target = head
        while current.next:
            if i > n:
                target = target.next
            else:
                i += 1
            current = current.next
        if i == n:
            head = head.next
        else:
            removed = None
            if target.next:
                removed = target.next.next
            target.next = removed
        return head