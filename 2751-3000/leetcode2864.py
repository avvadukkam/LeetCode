class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = s.count('0')
        ones = s.count('1') - 1
        return "".join(['1'] * ones + ['0'] * zeros + ['1'])