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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None or q is None:
            return p == q
        return (
            (p.val == q.val) and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )



root4 = TreeNode(4)
root3 = TreeNode(3)
root2 = TreeNode(2, right=root4)
root1 = TreeNode(1, root2, root3)

root_4 = TreeNode(4)
root_3 = TreeNode(3, root4)
root_2 = TreeNode(2)
root_1 = TreeNode(1, root_2, root_3)

print(Solution().isSameTree(root_1, root1))
