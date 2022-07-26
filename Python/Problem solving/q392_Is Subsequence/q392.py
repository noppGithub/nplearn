# iterate through t to find the first character of s
# when found, continue iteration over t looking for the next character of s
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
