from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 1 and len(t) == 1:
            return s == t
        return (Counter(s) == Counter(t)) and (s != t)

if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram")) #True
    print(s.isAnagram("a", "a")) #True