from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ================================= My method is too slow =================================
        # combinations = []
        # for index, num in enumerate(nums):
        #     for ij in range(index + 1, len(nums), 1):
        #         for ik in range(index + 2, len(nums), 1):
        #             if (0 == num + nums[ij] + nums[ik]) and (index != ij != ik):
        #                 combination = sorted([num, nums[ij], nums[ik]])
        #                 if combination not in combinations:
        #                     combinations.append(combination)
        # return combinations
        result = []
        nums.sort() #sort with n log n, but can use it to slide up and down
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            left,right = index+1,len(nums)-1 #setup 2 pointers
            while left < right:
                sum3 = num + nums[left]+nums[right]
                if sum3 > 0 :
                    right -= 1
                elif sum3 < 0:
                    left += 1
                else:
                    result.append([num,nums[left],nums[right]])
                    left += 1 #move left to the next item
                    
                    # handle the duplicate number in the input array
                    while (nums[left] == nums[left-1]) and (left < right):
                        left += 1
        return result



if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([1, 2, -2, -1]))
