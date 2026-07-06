# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        remainder = 0

        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + remainder

            digit = total % 10
            remainder = total // 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# July 6 2026
# Documentary: We check the if there l1, l2 and remainder as we traverse the linked list, then sum then as we pass and build our sum of linked list 
# Time complexity: O(max(n, m)
# Space complexity: O(1)
