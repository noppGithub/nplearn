class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        centres = [len(s) - 1]

        # create the list of indices from the longest to the shortest
        for diff in range(1, len(s)):
            centres.append(centres[0] + diff)
            centres.append(centres[0] - diff)
        for centre in centres:
            if min(centre + 1, 2 * len(s) - 1 - centre) <= len(
                longest_palindrome
            ):
                break  # stop if can't find a longer palindrome

            if centre % 2 == 0:
                left, right = (centre // 2) - 1, centre // 2 + 1
            else:
                left, right = (centre // 2), (centre // 2) + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now beyond the edge of the substring
            if right - left - 1 > len(longest_palindrome):
                longest_palindrome = s[left + 1 : right]

        return longest_palindrome


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
