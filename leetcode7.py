class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        reverse = int(str_x[::-1]) if x>=0 else -int(str_x[:0:-1])
        return reverse if -2147483648 <= reverse and reverse <= 2147483647 else 0
    