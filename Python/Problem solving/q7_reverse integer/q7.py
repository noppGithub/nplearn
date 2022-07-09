class Solution:
    def reverse(self, x: int) -> int:
        """Repeatedly multiply the previous result by 10 and add the last digit

        Args:
            x (int): input number in 32 bit signed integer format

        Returns:
            int: reversed number
        """
        negative = x < 0
        x = abs(x)
        reversed = 0
        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        if reversed > 2**31 - 1:
            return 0
        return reversed if not negative else -reversed


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
