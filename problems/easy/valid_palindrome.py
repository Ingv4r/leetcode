class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        left, right = 0, len(s) - 1
        while right >= left:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


print(Solution().isPalindrome("0P"))
