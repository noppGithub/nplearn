from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for operation in operations:
            if '+' in operation:
                value += 1
            else:
                value -= 1
        return value
        

if __name__ == "__main__":
    s = Solution()
    print(s.finalValueAfterOperations(["--X","X++","X++"]))