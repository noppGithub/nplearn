class Solution:
    def mySqrt(self, x: int) -> int:
        """
        // is the key to this problem, flooring division
        start by random a number from the input value
        if the number is too big, average to the previous random number
        when the random number is to high, x// random number will be too low.
        stop the process when the random number * random number  <= input value
        """
        randomnum = x
        while randomnum * randomnum > x:
            randomnum = (randomnum + x // randomnum) // 2
        return randomnum


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))
    print(s.mySqrt(9))
