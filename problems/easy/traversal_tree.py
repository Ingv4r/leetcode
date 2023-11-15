


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        left_res = []
        right_res = []
        prev_root = None
        while root.right or root.left:
            prev_root = root
            if root.right:
                left_res.append(root.val)
                root = root.right
            elif root.left:
                right_res.append(root.val)
                root = root.left
        if prev_root.left:
            left_res.append(root.val)
        elif prev_root.right:
            right_res.append(root.val)
        res = left_res + right_res
        return res


node3 = TreeNode(3)
node2 = TreeNode(2, left=node3)
node1 = TreeNode(1, right=node2)

print(Solution().inorderTraversal(node1))
