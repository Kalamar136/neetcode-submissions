# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        queue = [root] if root else []
        while queue:
            max_depth += 1
            queue_instance = queue.copy()
            for node in queue_instance:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queue.pop(0)
        
        return max_depth
