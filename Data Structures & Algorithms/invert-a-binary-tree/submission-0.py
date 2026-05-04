# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursively inverts a binary tree

        Args:
            root: [Treenode] = The input tree node

        Returns:
            inverted_node: [Treenode] = Head of the inverted binary tree

        Complexity Analysis:
            Time:
            Space:

        """

        # What do I do when the node is null?

        if not root:
            return None

        # What do I tell my children
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # How do I combine their results
        root.left = right
        root.right = left

        return root



