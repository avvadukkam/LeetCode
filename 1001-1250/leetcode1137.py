class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            tribN = [0, 1, 1]
            for i in range(3,n+1):
                tribN.append(tribN[i-1]+tribN[i-2]+tribN[i-3])
        return tribN[-1]