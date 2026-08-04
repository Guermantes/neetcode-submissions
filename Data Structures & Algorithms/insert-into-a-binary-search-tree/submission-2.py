# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)

        curr = root
        while curr != None:
            if val < curr.val and curr.left != None:
                curr = curr.left
            elif val < curr.val and curr.left == None:
                curr.left = TreeNode(val)
                return root
            if val > curr.val and curr.right != None:
                curr = curr.right
            elif val > curr.val and curr.right == None:
                curr.right = TreeNode(val)
                return root
        