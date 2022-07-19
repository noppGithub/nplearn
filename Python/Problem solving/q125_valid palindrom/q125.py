import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase
        allowed = re.sub("[^a-zA-Z0-9]", "", s.lower())
        left, right = 0, len(allowed) - 1
        # iterate through the string from the left and the right
        while left < right:
            if allowed[left] != allowed[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
