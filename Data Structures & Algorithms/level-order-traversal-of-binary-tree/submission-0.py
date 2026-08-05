# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue = deque()
        queue.append([root,0])
        result = []
        while queue:
            curr = queue.popleft()
            if len(result) <= curr[1]:
                result.append([])
            result[curr[1]] += [curr[0].val]
            if curr[0].left:
                queue.append([curr[0].left, curr[1]+1])
            if curr[0].right:
                queue.append([curr[0].right, curr[1]+1])

        return result