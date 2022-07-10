from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """Get the first string and the last then iterate through the first string of the input list
        and check if the first string of the input list is a prefix of the first string of the input list.

        Args:
            strs (List[str]): list of string

        Returns:
            str: the longest common prefix of the input list
        """
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while (i < len(first)) and (i < len(last)) and (first[i] == last[i]):
            i += 1
        return first[:i]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))

    print(s.longestCommonPrefix2(["flower", "flow", "flight"]))
