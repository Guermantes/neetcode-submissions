# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                prev = root
                curr = root.right
                if not curr.left:
                    root.val = curr.val
                    root.right = curr.right
                    return root
                while curr.left:
                    prev = curr
                    curr = curr.left

                root.val = curr.val
                prev.left = curr.right
                return root
            else:
                return root.left or root.right
            
        return root







        '''p_node = root
        prev_node = root
        while p_node != None:
            if p_node.val > key:
                prev_node = p_node
                p_node = p_node.left
            elif p_node.val < key:
                prev_node = p_node 
                p_node = p_node.right
            else:
                break

        if p_node == None:
            return root

        if p_node.left and p_node.right:
            prev = p_node
            curr = p_node.right
            if not curr.left:
                p_node.val = curr.val
                prev.right = None
                return root
            while curr.left:
                prev = curr
                curr = curr.left

            p_node.val = curr.val
            prev.left = None
        else:
            p_node = p_node.left or p_node.right

        return root'''