class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for n in s:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        for key,val in d.items():
            if val==1:
                return s.index(key)
        return -1
        
     