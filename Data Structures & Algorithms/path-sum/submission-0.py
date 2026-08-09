# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr = 0
        status = False

        def inorder(node):
            nonlocal curr, targetSum, status
            if not node:
                return

            curr += node.val
            if (not node.left) and (not node.right):
                if curr ==  targetSum:
                    status = True 
            else:
                inorder(node.left)
                if node.left:
                    curr -= node.left.val
                inorder(node.right)
                if node.right:
                    curr -= node.right.val

        inorder(root)
        return status
