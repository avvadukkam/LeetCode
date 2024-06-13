class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        arr = s.split(" ")
        if len(arr) != len(pattern):
            return False

        di = {}
        dic = {}
        for p,c in zip(pattern, arr):
            if p in di:
                if di[p] != c:
                    return False
            else:
                di[p] = c
            if c in dic:
                if dic[c] != p:
                    return False
            else:
                dic[c] = p
        return True