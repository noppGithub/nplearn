from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Make sure the pointer to the next index
        for using with the number that not equal to value
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
