class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1),len(word2))
        output = ''
        i = 0
        while i < minLen:
            output += word1[i] + word2[i]
            i += 1
        if len(word1) > len(word2):
            output += word1[i:]
        else:
            output += word2[i:]
        return output