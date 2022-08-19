from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the number in the given array
        count = Counter(nums)
        # slice the most common result by k, then return only the keys of them
        return [k for k, _ in count.most_common()[:k]]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([3, 0, 1, 0], 1))
