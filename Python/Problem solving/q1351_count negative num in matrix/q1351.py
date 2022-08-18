from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        row_index, col_index = 0, n_col - 1
        total_negative_nums = 0
        # because the description told us that the list is sorted in descending order
        # so we can check each row by, starting from the right most of each row
        # and when you found a negative number, that's mean below it is all negative numbers
        # use the image below to understand the logic of the sample input
        # +++-
        # +++-
        # ++--
        # ----
        while row_index < n_row and col_index >= 0:
            if grid[row_index][col_index] >= 0:
                row_index += 1
            else:
                total_negative_nums += n_row - row_index
                col_index -= 1
        return total_negative_nums


if __name__ == "__main__":
    s = Solution()
    print(
        s.countNegatives(
            [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        )
    )  # 8
