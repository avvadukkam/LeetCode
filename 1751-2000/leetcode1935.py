class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        textArray = text.split()
        brokenset = set(brokenLetters)
        count = 0
        
        for word in textArray:
            if not brokenset.intersection(word):
                count += 1
                
        return count