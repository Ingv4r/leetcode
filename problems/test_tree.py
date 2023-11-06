class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSame(root.left, root.right)

    def isSame(self, leftroot, rightroot):
        if leftroot is None and rightroot is None:
            return True
        if leftroot is None or rightroot is None:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(
            leftroot.right, rightroot.left
        )


cr = TreeNode(3)
cl = TreeNode(4)
bl = TreeNode(3)
br = TreeNode(4)
ar = TreeNode(2, cl, cr)
al = TreeNode(2, bl, br)
a = TreeNode(1, al, ar)

res = Solution()
print(res.isSymmetric(a))
