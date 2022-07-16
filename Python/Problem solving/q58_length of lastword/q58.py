class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if s is empty, return 0
        if s == "":
            return 0
        else:
            # split the string into words and work with the last one
            s = s.split()  # type: ignore
            return len(s[-1])
