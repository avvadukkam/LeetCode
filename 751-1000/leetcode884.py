class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        output = []
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        for i in s1:
            if s1.count(i) == 1 and i not in s2:
                output.append(i)
        for i in s2:
            if s2.count(i) == 1 and i not in s1:
                output.append(i)
        return output