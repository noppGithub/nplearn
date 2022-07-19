from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        current_max_word = 0
        for sentence in sentences:
            n_word = len(sentence.split())
            if n_word > current_max_word:
                current_max_word = n_word
        return current_max_word
            
        

if __name__ == "__main__":
    s = Solution()
    print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))