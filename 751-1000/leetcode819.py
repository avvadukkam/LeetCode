class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wordDict = {}
        delimiters  = ["!", "?", "'", ",", ";", "."]
        for delimiter in delimiters:
            paragraph = " ".join(paragraph.lower().split(delimiter))
        paragraph = paragraph.split()
        for word in paragraph:
            if word not in banned:
                if word not in wordDict:
                    wordDict[word] = 1
                else:
                    wordDict[word] += 1
        return max(zip(wordDict.values(), wordDict.keys()))[1]