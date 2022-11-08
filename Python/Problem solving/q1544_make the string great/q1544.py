class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) == 0:
                res.append(c)
            # if the adding char is upper and we already have the lower of this char in the list
            elif res[-1].upper() == c and res[-1].islower():
                res.pop()
            # if the adding char is lower and we already have the upper of this char in the list
            elif res[-1].lower() == c and res[-1].isupper():
                res.pop()
            else:
                res.append(c)
        res = ''.join(res)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.makeGood("leEeetcode"))