class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = {}
        s = {}
        for i in range(len(score)):
            temp[i] = score[i]
        score.sort(reverse=True)
        l =  len(score)
        if l>=1:
            s[score[0]]= "Gold Medal"
        if l>=2:
            s[score[1]] = "Silver Medal"
        if l>=3:
            s[score[2]] = "Bronze Medal"
        for i in range(3,len(score)):
            s[score[i]] = i+1
        for i in range(len(score)):
            score[i] = str(s[temp[i]])
        return score