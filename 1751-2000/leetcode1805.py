class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in range(len(word)):
            if word[i].isalpha():
                word = word.replace(word[i], ' ')
                
        word = word.split()
        
        unique_integers = set(int(num) for num in word if num.isdigit())
        
        return len(unique_integers)