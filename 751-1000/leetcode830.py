class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start, end = 0, 0
        output = []
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                end = i
                if end-start>=2:
                    output.append([start,i])
                start = i+1
        if len(s) - start >= 3:
            output.append([start, len(s)-1])
        return output