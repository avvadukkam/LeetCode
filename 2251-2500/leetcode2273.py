class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev_sorted_word = None

        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word != prev_sorted_word:
                res.append(word)
                prev_sorted_word = sorted_word

        return res