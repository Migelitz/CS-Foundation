# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1 
                node = node.next  
                list1 = list1.next

            elif list1.val >= list2.val:
                node.next = list2
                node = node.next 
                list2 = list2.next 

        node.next = list1 if list1 else list2 # To get the last node

        return dummy.next

# Time Complexity: O(n + m) Because comparing two list
# Space Complexity: O(1)
