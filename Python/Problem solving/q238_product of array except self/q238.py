from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize the result array with all 1
        output = [1] * len(nums)
        # calculate the prefix and postfix product

        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        # for postfix product, we need to reverse the array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
