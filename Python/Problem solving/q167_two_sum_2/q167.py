from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        left_index, right_index = 0, len(numbers) - 1
        while left_index < right_index:
            sum_val = numbers[left_index] + numbers[right_index]
            if sum_val > target:
                right_index -= 1
            elif sum_val < target:
                left_index += 1
            else:
                output.append(left_index + 1)
                output.append(right_index + 1)
                left_index += 1
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([2, 3, 4], 6))
    print(s.twoSum([-1, 0], -1))
    print(s.twoSum([5, 25, 75], 100))
