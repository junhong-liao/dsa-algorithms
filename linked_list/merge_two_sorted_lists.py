class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                head.next, list1 = list1, list1.next
            else:
                head.next, list2 = list2, list2.next
            head = head.next
        head.next = list1 or list2
        return res.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        res = head
        while list1 or list2:
            if not list1:
                head.next = list2
                return res.next
            if not list2:
                head.next = list1
                return res.next
            if list1.val <= list2.val:
                head.next = list1
                next_node = list1.next
                list1.next = None
                list1 = next_node
                head = head.next
            else:
                head.next = list2
                next_node = list2.next
                list2.next = None
                list2 = next_node
                head = head.next
        return res.next
