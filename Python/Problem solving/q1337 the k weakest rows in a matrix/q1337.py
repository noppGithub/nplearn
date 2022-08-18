from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        rows = sorted(range(m), key=lambda i: (mat[i], i))
        print(rows)
        del rows[k:]
        return rows


if __name__ == "__main__":
    s = Solution()
    print(
        s.kWeakestRows(
            mat=[
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            k=3,
        )
    )
