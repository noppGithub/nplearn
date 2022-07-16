from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        if carry:
            digits.insert(0, carry)
        return digits

    def plusOne2(self, digits: List[int]) -> List[int]:
        # start from the lowest important digit, replace it with 0 until we meet first non 9 which is incremented
        index = len(digits) - 1
        while index >= 0 and digits[index] == 9:
            digits[index] = 0
            index -= 1
        if index == -1:
            return [1] + digits
        else:
            return digits[:index] + [digits[index] + 1] + digits[index + 1 :]


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne2([9, 9]))
