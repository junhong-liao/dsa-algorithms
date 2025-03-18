class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prev = head, None
        while current:
            next_node, current.next = current.next, prev
            prev, current = current, next_node
        return prev