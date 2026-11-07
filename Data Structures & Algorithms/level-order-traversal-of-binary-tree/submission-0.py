# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            q = deque([[root]])
            result = [[root.val]]
            while q:
                next_level = []
                next_level_val = []
                level_set = q.popleft()

                for node in level_set:
                    next_level.append(node.left) if node.left else None 
                    next_level.append(node.right) if node.right else None
                    next_level_val.append(node.left.val) if node.left else None 
                    next_level_val.append(node.right.val) if node.right else None

                q.append(next_level) if next_level else None 
                result.append(next_level_val) if next_level else None

            return result 
        else:
            return []
        