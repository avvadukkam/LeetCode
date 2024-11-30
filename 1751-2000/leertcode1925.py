class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
                c_sqr = a*a + b*b
                c = int(sqrt(c_sqr))
                if c*c == c_sqr and c<=n:
                    count += 2
        return count