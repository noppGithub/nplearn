class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        def island_area(row_index, col_index):
            # this is the function to find the area of the island
            grid[row_index][col_index] = 0
            area = 1

            # check the four directions(up, down, left, right)
            for dr, dc in up_down_left_right:
                if 0 <= row_index + dr < rows and 0 <= col_index + dc < cols and grid[row_index + dr][col_index + dc] == 1:
                    # RECURSIVE case: to find the area of the island
                    area += island_area(row_index + dr, col_index + dc)
            # NON RECURSIVE case: when there is no more island, return the area
            return area

        # setup the grid
        rows, cols = len(grid), len(grid[0])
        up_down_left_right = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0 # initialize the max area

        # loop through the grid, if the grid is 1, find the area of the island
        # using depth first search, during the search process, set the grid to 0
        # for those 0 grid, it means that the island is already visited
        for row in range(rows):
            for col in range(cols):
                # check those islands that are 1
                if grid[row][col] == 1: 
                    max_area = max(max_area, island_area(row, col))

        return max_area 

if __name__ == "__main__":
    s = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))
