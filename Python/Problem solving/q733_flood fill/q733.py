from typing import List


class Solution:
    # DFS
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def dfs(i, j):
            image[i][j] = color
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != color: 
            dfs(sr, sc)
        return image


if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
