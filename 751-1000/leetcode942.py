class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        x,y=0,len(s)
        res = []
        for c in s:
            if c=="I":
                res.append(x)
                x+=1
            else:
                res.append(y)
                y-=1
        res.append(x)
        return res