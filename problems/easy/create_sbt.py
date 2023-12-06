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
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
            return root
        return None


nums = [-3, -2, -1, 0, 1, 2, 3]
root = Solution().sortedArrayToBST(nums)


