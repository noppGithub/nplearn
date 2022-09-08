from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # since the time series is moving from the left to the right
        # we start the 2 pointer from the left most to the right
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            # check if the trade is profitable
            if prices[l] < prices[r]:
                # calculate the current profit only when it's profitable
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # move the left pointer to the position of the right pointer
                l = r

            # move the right pointer to the next position
            r += 1
        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
