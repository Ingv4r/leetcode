class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


list1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
list2 = [1, 2, 2]
Solution().merge(list1, 6, list2, 3)
print(list1)
