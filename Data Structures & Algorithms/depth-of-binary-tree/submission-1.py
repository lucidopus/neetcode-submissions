# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursively finds the depth of a binary tree

        Args:
            root: [Treenode] = The input tree node

        Returns:
            max_depth: int = Max depth of the binary tree

        Complexity Analysis:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree

        """
        if not root:
            return 0

        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)

        return max(left_depth, right_depth)

