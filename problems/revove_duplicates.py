from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

    def rem2(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


nums1 = [1, 1, 2]  # -> 2, [1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # -> 5, [0,1,2,3,4]
nums3 = [1, 1]
nums4 = [0, 1]
nums5 = []

sol = Solution()
print(sol.removeDuplicates(nums1), nums1)
print(sol.removeDuplicates(nums2), nums2)

print(sol.rem2(nums1), nums1)
