# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a descendant of itself).”


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # if root is None, we can't go further, e.g. the node(0) has no left and right child
        if not root:
            return None  # type: ignore
        # if root is either p or q so either p or q is the LCA
        if root == p or root == q:
            return root

        # go deeper to the left side
        left = self.lowestCommonAncestor(root.left, p, q)  # type: ignore
        # go deeper to the right side
        right = self.lowestCommonAncestor(root.right, p, q)  # type: ignore

        # finally return
        if left and right:
            return root
        return left if left else right


if __name__ == "__main__":
    s = Solution()
    # this one is easier to understand
    # create the tree
    root = TreeNode(3)
    root.left = TreeNode(5)  # type: ignore
    root.right = TreeNode(1)  # type: ignore
    root.left.left = TreeNode(6)  # type: ignore
    root.left.right = TreeNode(2)  # type: ignore # type: ignore
    root.left.right.left = TreeNode(7)  # type: ignore
    root.left.right.right = TreeNode(4)  # type: ignore
    root.right.left = TreeNode(0)  # type: ignore
    root.right.right = TreeNode(8)  # type: ignore

    # answer the question
    answer1 = s.lowestCommonAncestor(root, root.left, root.right)

    # answer the harder question
    answer2 = s.lowestCommonAncestor(root, root.left, root.left.right.right)
