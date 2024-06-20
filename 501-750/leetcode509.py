class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        cache[0] = 0
        if N==1 or N==2:
            cache[N] = 1
            return cache[N]
        elif N in cache:
            return cache[N]
        result = self.fib(N-1) + self.fib(N-2)
        cache[N] = result
        return result