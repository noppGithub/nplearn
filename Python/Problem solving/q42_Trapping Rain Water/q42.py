# this problem need you to know the fact that to trap a water
# at each position you will use the equattion `min(L,R) - h[i]` to determin the volumn of water you can trap
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        res = 0
        left_max, right_max = height[l], height[r]
        while l < r:
            # update the pointer on the side that has min value
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += self.calculate_water(left_max, height[l])

            else:
                r -= 1
                right_max = max(right_max, height[r])
                res+=self.calculate_water(right_max, height[r])
        return res

    def calculate_water(self,val_max,val_at_position):
        x = val_max - val_at_position
        if x > 0:
            return x
        return 0

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))