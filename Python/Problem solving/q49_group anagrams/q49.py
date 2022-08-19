from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = defaultdict(list)
        for word in strs:
            # Create a handmade Counter that hashable since it's tuple
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1 #add 1 to the index of the character
            memory[tuple(count)].append(word) #add it to the memory
        return memory.values()  # type: ignore

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # my own way, since I never know that ord() is the better counter for a-z
        memory = defaultdict(list)
        for word in strs:
            count = Counter(word)
            memory[tuple(sorted(count.items()))].append(word)
        return memory.values()  # type: ignore


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
