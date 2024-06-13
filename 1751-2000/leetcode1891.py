class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        word = ''.join(words)
        setWord = list(set(word))
        
        for i in range(len(setWord)):
            if word.count(setWord[i])%len(words) != 0 or word.count(setWord[i]) == 1:
                return False
        return True