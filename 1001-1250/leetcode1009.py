class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binNum = str(bin(n))[2:]
        comp = ''.join('1' if i=='0' else '0' for i in binNum)
        return int(comp,2)