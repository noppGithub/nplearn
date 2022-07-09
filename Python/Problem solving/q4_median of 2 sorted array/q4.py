from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2 # combine the two array
        nums.sort() #sort it if needed
        if len(nums) % 2 == 0: #check if the length is even
            # if even, return the average of the two middle numbers using index of the list
            return (nums[len(nums)//2] + nums[len(nums)//2-1])/2
        else:
            # if odd, return the middle number using index of the list
            return nums[len(nums)//2]

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,2],[3,4]))

        