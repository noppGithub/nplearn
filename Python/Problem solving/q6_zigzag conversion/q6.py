class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """build a list of characters for each row by tracking the 
        direction of movement up or down and reversing direction at end row.

        Time: O(n), use a list of chars and join instead of concatenating to immutable string
        Space: O(n), use a list of chars

        Args:
            s (str): the input string
            numRows (int): the number of rows required

        Returns:
            str: output string
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]
        else:
            rows = [''] * numRows
            row_index = 0
            direction = 1
            for c in s:
                rows[row_index] += c
                row_index += direction
                if row_index == numRows - 1:
                    direction = -1
                elif row_index == 0:
                    direction = 1
            return ''.join(rows)

if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
