# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current = headA
        seen = dict()

        while current:
            seen[current] = current
            current = current.next
        
        current = headB
        while current:
            if current in seen:
                return current
            current = current.next
        return None

# Time Complexity: O(m + n)
# Space Complexity: O(n) -> Not most optimal due to use of dictionary (hash map)