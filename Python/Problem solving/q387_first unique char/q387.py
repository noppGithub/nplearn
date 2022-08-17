class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create a dictionary to store the frequency of each character in the string
        char_counter = {}

        # iterate over each input character, add frequency = 1 if not in the dictionary, otherwise increase the frequency by 1
        for char in s:
            if char not in char_counter:
                char_counter[char] = 1
            else:
                char_counter[char] += 1

        # iterate over the dictionary and return the index of the first character with frequency = 1
        for index in range(len(s)):
            if char_counter[s[index]] == 1:
                return index

        # if none of the characters have frequency = 1, return -1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("aabb"))
