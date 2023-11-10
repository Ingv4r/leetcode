class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits
    

n1 = [1, 2, 3]
n2 = [9]
n3 = [9, 9]

sol = Solution()
assert sol.plusOne(n1) == [1, 2, 4]
assert sol.plusOne(n2) == [1, 0]
assert sol.plusOne(n3) == [1, 0, 0]
