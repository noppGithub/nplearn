from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        my_dict = {}
        n_good_pair = 0
        for number in nums:
            if number in my_dict:
                n_good_pair += my_dict[number]
                my_dict[number] += 1
            else:
                my_dict[number] = 1
        return n_good_pair


if __name__ == "__main__":
    s = Solution()
    print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
