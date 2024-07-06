class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")
    
        if s[-1][-1] != s[0][0]:
            return False
        for i in range(len(s)-1):
            if s[i][-1] != s[i+1][0]:
                return False
        return True