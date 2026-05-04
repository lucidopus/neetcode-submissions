# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Checks if two binary trees are the same

        Args:
            p: [Treenode] = The first tree
            q: [Treenode] = The second tree

        Returns:
            isSame: bool = Returns True of the trees are same or else False

        Complexity Analysis:
            Time: O(n) where n is the number of nodes
            Space: O(n)

        """

        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)

        return isLeftSame and isRightSame

