class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        while n!=0:
            if n%2==0:
                res.append(n)
                res.append(-n)
                n-=2
            else:
                res.append(0)
                n-=1
        return res