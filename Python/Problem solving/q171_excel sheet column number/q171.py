class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for i in range(len(columnTitle)):
            col_num += (ord(columnTitle[i]) - ord('A') + 1) * 26 ** (len(columnTitle) - i - 1)
        return col_num

    # ================================= easy to read version =================================
    def titleToNumber2(self, columnTitle: str) -> int:
        """loop over the string and add the value of the character to the result

        Args:
            columnTitle (str): input column name

        Returns:
            int: number of column
        """
        col_num = 0
        for i in range(len(columnTitle)):
            # ord('Z') = 90, ord('A') = 65, so we need to plus 1 to get the value of the character
            # multiply each character by 26^(length of the string - 1 - i)
            col_num += self.get_char_value(
                columnTitle[i]
            ) * 26 ** self.get_power(len(columnTitle), i)
        return col_num

    def get_char_value(self, char: str) -> int:
        # get the value of the character using ord()
        return ord(char) - ord("A") + 1

    def get_power(self, charlength: int = 2, index: int = 0) -> int:
        # calculate the power of character digit
        return charlength - index - 1
        

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))
    print(s.titleToNumber("ZY"))
    print(s.titleToNumber2("ZY"))