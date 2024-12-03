class Solution:
    def minTimeToType(self, word: str) -> int:
        count = len(word)
        word = 'a' + word
        for i in range(1,len(word)):
            distance = abs(ord(word[i])-ord(word[i-1]))
            count += min(distance, 26-distance)
        return count
    

# Optimized
class Solution:
    def minTimeToType(self, word: str) -> int:
        count = len(word)
        prev = 'a'

        for char in word:
            distance = abs(ord(char)-ord(prev))
            count += min(distance, 26-distance)
            prev = char
            
        return count