# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            # check if the number is a starter of a sequence
            if (num - 1) not in numset:
                current_length = 1
                # since it's starting number of a sequence, find the length of the sequence
                while (num + current_length) in numset:
                    current_length += 1

                # keep update the legnth of the longest sequence
                longest = max(current_length, longest)
        return longest

    def longestConsecutive2(self, nums: List[int]) -> int:
        # this method exploits the fact that sequence is +1 or -1,
        # so we can use minus to find the distance between the first item and the last item in sequence
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                next_val = num + 1
                while next_val in nums:
                    next_val += 1
                longest = max(longest, next_val - num)
        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive2([100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive2([1, 2, 0, 1]))
