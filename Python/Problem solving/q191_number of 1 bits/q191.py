class Solution:
    def hammingWeight(self, n: int) -> int:
        print(f"We start with count = 0, and the input number is {n}")
        count = 0
        # while it's greater than zero

        print(f"We add 1 to count if it's greater than 0")
        print("=" * 20)
        while n:
            print(f"integer number is {n} > 0, we add 1 to count")
            count += 1

            # we remove the right most 1 from n, you may call it least significant 1
            print(f"Now my integer in bit is: {bin(n)[2:]}")

            n_next = n - 1
            print(f"Now integer minus 1 in bit is: {bin(n_next)[2:]}")

            n = n & n_next
            print(f"Use & operation to remove the least significant 1")
            print(f"Now our integer in bit is: {bin(n)[2:]}")
            print("=" * 20)

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(11))
