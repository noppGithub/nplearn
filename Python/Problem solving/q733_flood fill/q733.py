# we will do the jon only when the input color(number) is different from the current color
# we need to recursively call the function to fill the color
from typing import List


class Solution:
    # DFS
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """check if the current color is different from the input color
        if it is different, we will change the color to the input color using depth first search(recursion)

        Args:
            image (List[List[int]]): array of image
            sr (int): starting row
            sc (int): starting column
            color (int): color to be filled

        Returns:
            List[List[int]]: array of image
        """
        def dfs(row_index, col_index):
            image[row_index][col_index] = color #fill the input color to the cell
            # look at the cell below,above,left,right
            for row_index_next, col_index_next in ((row_index - 1, col_index), (row_index + 1, col_index), (row_index, col_index - 1), (row_index, col_index + 1)):
                # check if the cell is still in the range of the input image + check if the cell color is the same as the existing color that requires to be filled
                if 0 <= row_index_next < total_rows and 0 <= col_index_next < total_columns and image[row_index_next][col_index_next] == existing_color:
                    dfs(row_index_next, col_index_next)
        existing_color, total_rows, total_columns = image[sr][sc], len(image), len(image[0])
        if existing_color != color: 
            dfs(sr, sc)
        return image


if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))