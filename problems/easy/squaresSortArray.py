class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sol = list(map(lambda x: x**2, nums))
        return sorted(sol)


nums = [-4, -1, 0, 3, 10]
s = Solution().sortedSquares(nums)
print(s)
