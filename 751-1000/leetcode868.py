class Solution:
    def binaryGap(self, n: int) -> int:
        binN = str(bin(n)[2:])
        res = []
        count = 1
        if binN.count('1') == 1:
            return 0
        else:
            for i in binN:
                if i=='0':
                    count+=1
                else:
                    res.append(count)
                    count = 1

        return max(res)
    