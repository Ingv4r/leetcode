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
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return (
                self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val)
        )




r2 = TreeNode(2)
r3 = TreeNode(3)
root = TreeNode(1, r2, r3)

print(Solution().hasPathSum(root, 6))
