from typing import List


class Solution:
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

n1 = [3, 2, 2, 3]  # -> [2, 2, _, _]
n2 = [0, 1, 2, 2, 3, 0, 4, 2]  # -> [0, 1, 3, 0, 4, _, _, _]

sol = Solution()
print(sol.removeElement(n1, 3))
print(sol.removeElement(n2, 2))
