"""Document."""


class Solution:
    """A class."""

    def removeStars(self, s: str) -> str:
        """Aefewf efw."""
        ans = []
        for i in s:
            if i == "*":
                ans.pop()
            else:
                ans += [i]
        return "".join(ans)


sol = Solution()
print(sol.removeStars("erase*****"))
print(sol.removeStars("leet**cod*e"))
print(sol.removeStars("abb*cdfg*****x*"))
with open("fuckingtext.txt", "r") as f:
    text = f.read()
print(sol.removeStars(text))
with open("fuckingtext2.txt", "r") as f:
    text2 = f.read()
print(sol.removeStars(text2))
