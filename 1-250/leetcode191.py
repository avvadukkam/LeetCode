class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        n = '%32s' % n
        n = n.replace(' ','0')
        n = str(n)
        count = 0
        for s in n:
            if s == "1":
                count += 1
        return count