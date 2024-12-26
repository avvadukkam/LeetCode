class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        words_dic = Counter(words)
        count = 0

        for i in range(len(s)):
            if s[:i+1] in words_dic:
                count += words_dic[s[:i+1]]
        return count