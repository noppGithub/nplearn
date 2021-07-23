from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_number_index = {}
        for index, number in enumerate(nums):
            num_to_target = target - number
            if num_to_target in seen_number_index:
                return [seen_number_index[num_to_target],index]
            seen_number_index[number] = index
        return [] 

if __name__ == "__main__":
    s = Solution()
    array = s.twoSum([2,7,11,15],9)
    print(array)