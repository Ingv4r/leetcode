"""Document."""


def simplifyPath(path: str) -> str:
    """Return canonical path in a Unix-style file system."""
    s_list = path.split("/")
    s_list = [i for i in s_list if i and i != "."]
    res = ""
    while ".." in s_list:
        index = s_list.index("..")
        s_list.pop(index)
        if index != 0:
            s_list.pop(index - 1)

    for i in s_list:
        res += "/" + i
    return res if s_list else "/"


paths = ("/a/./b/../../c/", "/../", "/home", "/home//..", "/a/../../b/../c//.//", "/")
debug = ("/.///../JY", "///eHx/..")
for path in paths:
    print(simplifyPath(path))

print(all(str(None)))
