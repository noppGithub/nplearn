import re


class Solution:
    # ================================= 2 pointers method =================================
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

    def isPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # ================================= string reverse =================================
    def isPalindrome3(self, s: str) -> bool:
        new_str = [ch.lower() for ch in s if ch.isalnum()]
        return new_str == new_str[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
