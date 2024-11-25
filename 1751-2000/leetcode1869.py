class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s0 = s.split('1')
        s1 = s.split('0')
        maxLenS0 = max(len(i) for i in s0)
        maxLenS1 = max(len(i) for i in s1)

        return maxLenS1 > maxLenS0