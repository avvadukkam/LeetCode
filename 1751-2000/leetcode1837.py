class Solution:
    def sumBase(self, n: int, k: int) -> int:
        nBk_sum = 0
        while n > 0:
            nBk_sum += n%k
            n //= k
        return nBk_sum