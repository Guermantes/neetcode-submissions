# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = k
        kvalue = -1

        def inorder(node: Optional[TreeNode]):
            nonlocal count, kvalue
            if not node or kvalue != -1:
                return

            inorder(node.left)
            if kvalue == -1:
                count -= 1
                if count == 0:
                    kvalue = node.val
                    return
                inorder(node.right)

        inorder(root)
        return kvalue