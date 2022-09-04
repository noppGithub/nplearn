# start the left and right pointers on the given array
# keep calculate the area of the water container
# if the height of the water container left is less than the height of the the right, shift the left pointer
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            # กว้าง * สูง
            size = (r - l) * min(height[l], height[r])
            res = max(res, size)
            if height[l] < height[r]:
                l += 1  # increase the left pointer
            else:
                r -= 1  # decrease the right pointer
        return res
