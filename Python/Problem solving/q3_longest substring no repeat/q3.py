class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        last_seen_char = {}  # store the last seen character
        for index, char in enumerate(s):
            if char in last_seen_char and start <= last_seen_char[char]:
                start = (
                    last_seen_char[char] + 1
                )  # update start index using the last seen character from `last_seen_char`
            else:
                max_length = max(max_length, index - start + 1)
            last_seen_char[char] = index
        return max_length


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcxyzbb"))
