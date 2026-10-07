# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        def maxdepth(root,d):
            if root is None:
                return d
            return max(maxdepth(root.left,d+1),maxdepth(root.right,d+1))

        depth = maxdepth(root,0)
        return depth
