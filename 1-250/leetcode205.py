class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS , mapT = {}, {}
        for a, b in zip(s,t):
            if ((a in mapS and mapS[a] != b) or (b in mapT and mapT[b] != a)):
                return False
            mapS[a] = b
            mapT[b] = a
        return True
        