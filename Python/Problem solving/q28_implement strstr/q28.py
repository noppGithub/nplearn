class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index : index + len(needle)] == needle:
                return index
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        """
        Find the first index of the needle in the haystack
        """
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    def strStr3(self, haystack: str, needle: str) -> int:
        """check the possible starting point in haystack
        check if it's the same as needle, break if it's not match
        """
        for index in range(len(haystack) - len(needle) + 1):
            for index2 in range(len(needle)):
                if haystack[index + index2] != needle[index2]:
                    break
            else:
                return index
        return -1
