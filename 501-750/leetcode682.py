class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == 'C':
                score.pop()
            elif i == 'D':
                score.append(score[-1]*2)
            elif i == "+":
                score.append(score[-1] + score[-2])
            elif i.isdigit() or i.startswith('-') and i[1:].isdigit(): # or just use "else"
                score.append(int(i))
        return sum(score)