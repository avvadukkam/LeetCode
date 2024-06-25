class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c,x):
            return chr(ord(c)+int(x))
        s = list(s)
        for i in range(len(s)):
            if s[i].isdigit():
                s[i] = shift(s[i-1], s[i])
        return ''.join(s)