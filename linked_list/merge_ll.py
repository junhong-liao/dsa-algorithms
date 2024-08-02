from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return res.next

    # def mergeTwoLists_v0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     head = ListNode()
    #     current = head
    #     while l1 or l2:
    #         if not l1:
    #             while l2:
    #                 current.next = l2
    #                 current, l2 = current.next, l2.next
    #             break
    #         if not l2:
    #             while l1:
    #                 current.next = l1
    #                 current, l1 = current.next, l1.next
    #             break
    #         if l1.val <= l2.val:
    #             current.next = l1
    #             l1 = l1.next
    #         else:
    #             current.next = l2
    #             l2 = l2.next
    #     return head.next

s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(5)))
res = s.mergeTwoLists(list1, list2)
current = res
while current:
    print(current.val, end='')
    current = current.next

# Output: [1,1,2,3,4,5]


