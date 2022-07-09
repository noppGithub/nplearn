class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dynamic programming calculation of matrix of whether any prefix of s patches any prefix of p
        matched = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        matched[0][0] = True
        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                pattern = p[j-1]
                if pattern == '.': # dot matches any last character of s
                    matched[i][j] = (i != 0 and matched[i-1][j-1])
                elif pattern == '*': # ignore last 2 characters of p OR ignore the last character of s
                    star = p[j-2] # match the star character
                    matched[i][j] = matched[i][j-2] or (i > 0 and matched[i-1][j] and (star == s[i-1] or star == '.'))
                else: # the pattern must match the last character of s
                    matched[i][j] = (i != 0 and matched[i-1][j-1] and pattern == s[i-1])
        return matched[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch("ab", ".*"))