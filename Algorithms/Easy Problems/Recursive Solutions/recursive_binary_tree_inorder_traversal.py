# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = list()
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root is None:
            return
        self.helper(root.left, ans)
        ans.append(root.val)
        self.helper(root.right, ans)
      
# Time complexity: O(n) traverse nodes once so linear time
# Space complexity: O(1) even list is declared once, but the problem is call stack; best case O(log n) and worst case O(n)
