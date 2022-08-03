from typing import List

import numpy as np

# comment numpy in line 3 and 11 to run without numpy


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ## show the grid as matrix for better understanding
        print(np.matrix(grid))

        # setup the parameters before traversing the grid
        total_closed_island = 0
        self.visited = set()
        self.total_rows = len(grid)
        self.total_cols = len(grid[0])

        # traverse the grid by row and column
        for row_index in range(self.total_rows):
            for col_index in range(self.total_cols):
                # we focus on land which is 0, and check if they are not visited
                if (grid[row_index][col_index] == 0) and (
                    (row_index, col_index) not in self.visited
                ):
                    is_closed_island = self.dfs(grid, row_index, col_index)
                    total_closed_island += 1 if is_closed_island else 0
        return total_closed_island

    def dfs(self, grid, row_index, col_index):
        # check both row_index and col_index if they are out of range, OR at the edge
        if (
            row_index < 0
            or row_index == self.total_rows
            or col_index < 0
            or col_index == self.total_cols
        ):
            return False
        # if it's land, return True
        if grid[row_index][col_index] == 1:
            return True
        # if this cell is visited, return True
        if (row_index, col_index) in self.visited:
            return True

        # mark this cell as visited
        self.visited.add((row_index, col_index))

        # traverse the four directions
        top = self.dfs(grid, row_index - 1, col_index)
        bottom = self.dfs(grid, row_index + 1, col_index)
        left = self.dfs(grid, row_index, col_index - 1)
        right = self.dfs(grid, row_index, col_index + 1)

        # use and to check if all four directions are True, which is the closed island
        return top and bottom and left and right


if __name__ == "__main__":
    s = Solution()
    print(
        s.closedIsland(
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ]
        )
    )
