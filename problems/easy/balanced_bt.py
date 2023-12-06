class Solution():
    def isBalanced(self, root):
        return self.Height(root) >= 0

    def Height(self, root):
        if not root:
            return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1
