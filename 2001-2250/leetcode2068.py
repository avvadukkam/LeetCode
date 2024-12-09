class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        word2_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        for letter in word1:
            word1_dict[letter] += 1
        for letter in word2:
            word2_dict[letter] += 1
        
        for word, count in word1_dict.items():
            if abs(word1_dict[word] - word2_dict[word]) >3:
                return False
        return True
    
# Optimized Version
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        all_chars = set(count1.keys()).union(count2.keys())
        
        for char in all_chars:
            if abs(count1[char] - count2[char]) >3:
                return False
        
        return True