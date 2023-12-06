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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left

            root = st.pop()
            res.append(root.val)

            root = root.right

        return res

def make_tree():
    data = [2, 3, None, 1]
    root = TreeNode(data[0])
    res = [root]
    for i in range(len(data) - 2):
        res[i].left = TreeNode(data[i + 1])
        res[i].right = TreeNode(data[i + 2])
        if data[i+1]:
            root = res[i].left
        elif data[i+2]:
            root = res[i].right
        res.append(root)
    res[-1].val = data[-1]
    return res[0]


root3 = TreeNode(3)
root2 = TreeNode(2, left=root3)
root1 = TreeNode(1, right=root2)
print(Solution().inorderTraversal(root1))
