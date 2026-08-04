# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversed = []
        if not root:
            return []
        traversed.extend(self.inorderTraversal(root.left))
        traversed.append(root.val)
        traversed.extend(self.inorderTraversal(root.right))
        return traversed