class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = []
        res = []
        for c in words[0]:
            for i in range(len(words)):
                if c in words[i]:
                    temp.append(c)
                    words[i] = words[i][:words[i].index(c)]+words[i][words[i].index(c)+1:]
                if len(temp) == len(words):
                    res.append(c)
            temp = []
        return res