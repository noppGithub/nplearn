from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        output = [self.is_valid(x,arr2,d) for x in arr1]
        return sum(output)

    def is_valid(self,val,arr2,d):
        # use this function to check if the whole matrix is valid
        l, r = 0, len(arr2)
        while l < r:
            mid = (l + r) // 2
            if abs(arr2[mid] - val) <= d:
                return False
            elif arr2[mid] > val:
                r = mid
            else:
                l = mid + 1
        return True

if __name__ == "__main__":
    x = Solution()
    print(x.findTheDistanceValue([4,5,8],[10,9,1,8],2))