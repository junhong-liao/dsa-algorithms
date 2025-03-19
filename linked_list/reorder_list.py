from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second = slow.next
        slow.next = None
        
        # reverse the second half

        current, prev = second, None
        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node
        # second = prev

        
