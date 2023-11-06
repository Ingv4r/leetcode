class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in valid:
                stack.append(c)
            elif not stack:
                return False
            elif c == valid[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack


if __name__ == "__main__":
    s = Solution().isValid("")
    print(s)
