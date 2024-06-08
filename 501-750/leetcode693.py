class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bN = "{0:b}".format(n)
        output = True
        for i in range(1,len(bN)):
            if int(bN[i-1]) != 1 - int(bN[i]):
                output = False
        return output