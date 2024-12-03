class Solution:
    def minTimeToType(self, word: str) -> int:
        count = len(word)
        word = 'a' + word
        for i in range(1,len(word)):
            distance = abs(ord(word[i])-ord(word[i-1]))
            count += min(distance, 26-distance)
        return count