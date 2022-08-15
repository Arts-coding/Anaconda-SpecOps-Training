def strStr(needle, haystack):

    if len(needle) <= len(haystack):
        if needle in haystack:
            return haystack.index(needle[0])
        return -1
    else:
        if haystack in needle:
            return needle.index(haystack[0])
        return -1

print(strStr("ab", "aba")) 