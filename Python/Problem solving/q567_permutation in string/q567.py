import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # guardian
        if s1 == s2:
            return True
        if len(s1) == 0 or len(s2) == 0:
            return False

        # anagram searching
        cnt1, cnt2 = collections.Counter(s1), collections.Counter(s2[:len(s1)])
        for index in range(len(s1), len(s2)):
            if cnt1 == cnt2: 
                return True

            cnt2[s2[index]] += 1 #add next char of s2 to the counter
            cnt2[s2[index-len(s1)]] -= 1 #remove the first char of s2 from the counter

            if cnt2[s2[index-len(s1)]] == 0: # remove the key if its value is 0
                del cnt2[s2[index-len(s1)]]
        return cnt1 == cnt2 
        
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))