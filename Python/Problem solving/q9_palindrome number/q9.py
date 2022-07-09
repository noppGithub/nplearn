class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if the first and the last character are the same, moving towards the middle
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        # check if the first and the last character are the same, moving towards the middle
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(13241))

    print(s.isPalindrome2(121))
    print(s.isPalindrome2(13241))
