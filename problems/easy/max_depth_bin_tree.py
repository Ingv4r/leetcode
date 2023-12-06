class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        left_val = self.left.val if self.left else None
        right_val = self.right.val if self.right else None
        return f"({self.val}, left={left_val}, right={right_val}) "


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


root5 = TreeNode(5)
root4 = TreeNode(4)
root3 = TreeNode(3, root4, root5)
root2 = TreeNode(2)
root = TreeNode(1, root2, root3)

print(Solution().maxDepth(root))
