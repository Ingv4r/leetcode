class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                k += 1
        return k


l = [1, 1, 2, 1]
s = Solution().removeDuplicates(l)
print(s)
