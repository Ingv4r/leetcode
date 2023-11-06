import unittest


def rle3(s):
    i, res = 0, []
    while i < len(s):
        cnt = 1
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                j += 1
                cnt += 1
            else:
                break

        res.append(s[i])
        if cnt > 1:
            res.append(str(cnt))
        i = j
    return "".join(res)


if __name__ == "__main__":
    assert rle3("AABB") == "A2B2"
