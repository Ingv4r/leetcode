from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums = Counter(nums)
        return nums.most_common()[-1][0]


print(Solution().singleNumber([2, 2, 1]))
