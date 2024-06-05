class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        word_len = len(words) 
        count = 0
        for i in range(word_len):
            for j in range(i+1, word_len):
                prefix = words[i]
                if len(prefix) <= len(words[j]) and prefix == words[j][:len(prefix)] == words[j][-len(prefix):]:
                    count += 1
            
        return count