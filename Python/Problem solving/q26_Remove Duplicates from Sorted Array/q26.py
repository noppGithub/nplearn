from typing import List


# keep update the pointer at the next index to fill with a new number
# check those next numbers versus the previous numbers
# if any of them different, move it to the next new index
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_number = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[next_number] = nums[i]
                next_number += 1
        return next_number


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))
