import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        cnt = Counter(words)
        output = cnt.most_common(k)
        output = [x[0] for x in output]
        return output

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        words.sort()
        cnt = Counter(words)
        output = heapq.nsmallest(k, cnt, key=lambda word: (~cnt[word], word))
        return output


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    s = Solution()
    print(s.topKFrequent(words, k))
    print(s.topKFrequent2(words, k))

    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    s = Solution()
    print(s.topKFrequent(words, k))
    print(s.topKFrequent2(words, k))
