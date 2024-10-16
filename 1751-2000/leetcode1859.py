class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        temp = ['']*len(s)
        for word in s:
            temp[int(word[-1])-1] = word[:-1]
            
        return ' '.join(temp)