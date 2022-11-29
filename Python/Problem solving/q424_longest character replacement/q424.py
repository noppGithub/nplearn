class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        max_length = 0

        # start 2 pointers
        l = 0
        # iterate over the r pointer to create a sliding window
        for r in range(len(s)):
            # add freq count to the hash table, return 0 if not exist
            counter[s[r]] = counter.get(s[r], 0) + 1

            # set the window and check if the most frequent char is greater than k
            # the current window is (r-l+1) and the most frequent char is max(char_freq_count.values())
            # we are looking for the longest window that WINDOW_LENGTH - MOST_FREQ_CHAR <= K
            # use while loop to shrink the window until the condition is met
            # then we move the l pointer to the right and repeat the process
            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1  # move the left pointer

            max_length = max(max_length, (r - l + 1))
        return max_length


if __name__ == "__main__":
    s = Solution()
    # print(s.characterReplacement("ABAB", 2))
    print(s.characterReplacement("AABABBA", 1))
