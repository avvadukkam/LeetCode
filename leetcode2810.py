class Solution:
    def finalString(self, s: str) -> str:
        t= ""
        for i in s:
            if i == 'i':
                t = t[::-1]
            else:
                t += i 
        return t