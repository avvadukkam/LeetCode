class Solution:
    def thousandSeparator(self, n: int) -> str:
        strN = str(n)
        for i in range(len(strN)-3,0,-3):
            strN = strN[:i]+'.'+strN[i:]
        return strN