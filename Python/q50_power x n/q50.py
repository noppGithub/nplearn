class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

    # ================================= method 2 =================================
    """
    recursive method, 
    """

    def myPow2(self, x: float, n: int) -> float:
        is_negative = n < 0
        pos_result = self.helper(x, abs(n))
        if is_negative:
            return 1 / pos_result
        return pos_result

    def helper(self, x: float, n: int) -> float:
        """This function will recursively call itself
        to calculate the x power by n, it will hit the n==0 then start to return the result
        take the result and calculate it back to the original x
        e.g. n = 0, x = 2, result = 1
        e.g. n = 1, x = 2, result = 2
        whenever n is odd, result = result * x (e.g. n=1, x=2, result=2)

        Args:
            x (float): base number
            n (int): power number

        Returns:
            float: base ** power
        """
        print(f"The input is {x} and {n}")
        if n == 0:
            return 1
        temp = self.helper(x, n // 2)
        temp *= temp
        if n % 2 == 1:
            temp *= x
        return temp


if __name__ == "__main__":
    s = Solution()
    print(s.myPow2(2.00000, -2))
