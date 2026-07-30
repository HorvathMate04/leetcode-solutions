"""Given the head of a linked list head, 
in which each node contains an integer value.

Between every pair of adjacent nodes, insert 
a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is 
the largest positive integer that evenly divides both numbers."""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current.next:
            node = ListNode(self.findGreatestCommonDivisor(current.val, current.next.val), current.next)
            current.next = node
            current = node.next
        return head


    def findGreatestCommonDivisor(self, num1, num2):
        if num2 == 0:
            return num1
        return self.findGreatestCommonDivisor(num2, num1%num2)