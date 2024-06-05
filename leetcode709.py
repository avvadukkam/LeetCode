class Solution:
    def toLowerCase(self, s: str) -> str:
        t=""
        for i in s:
            if 65<=ord(i) and ord(i)<=90:
                t+= chr(ord(i)+32)
            else:
                t+=i
        return t