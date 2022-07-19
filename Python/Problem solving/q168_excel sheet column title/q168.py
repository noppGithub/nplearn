class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """generate character from the remainder of the division of columnNumber by 26
        and add the character to the result string

        Args:
            columnNumber (int): _description_

        Returns:
            str: _description_
        """
        column = []
        while columnNumber > 0:
            columnNumber, r = divmod(columnNumber - 1, 26)
            column.append(chr(r + ord("A")))

        return "".join(reversed(column))


if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(1))
    print(s.convertToTitle(28))
    print(s.convertToTitle(701))  # this one kill my previous solution
