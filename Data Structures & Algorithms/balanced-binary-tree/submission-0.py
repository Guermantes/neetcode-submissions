# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        b = True

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            if not node.left:
                node.lheight = 0
            else:
                dfs(node.left)
                node.lheight = max(node.left.lheight, node.left.rheight) + 1

            if not node.right:
                node.rheight = 0
            else:
                dfs(node.right)
                node.rheight = max(node.right.lheight, node.right.rheight) + 1
            
            nonlocal b
            if node.lheight > node.rheight + 1 or node.lheight < node.rheight - 1:
                b = False

        dfs(root)
        return b
            
            
