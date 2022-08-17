from multiprocessing.sharedctypes import Value
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> Optional[bool]:
        # represent the leaf node
        if root.val == 0:
            return False
        # represent the leaf node
        elif root.val == 1:
            return True

        # represent non-leaf node
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(
                root.right
            )
        else:
            raise Exception(f"Invalid input: {root.val}")


if __name__ == "__main__":
    s = Solution()
    # test case 1
    print(
        s.evaluateTree(
            TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
        )
    )
    # test case 2
    print(s.evaluateTree(TreeNode(0)))
    # test case 3, changed 213 to 203
    print(
        s.evaluateTree(
            TreeNode(2, TreeNode(0), TreeNode(3, TreeNode(0), TreeNode(1)))
        )
    )
