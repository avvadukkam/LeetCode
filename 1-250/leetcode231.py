class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a,b = 1,1
        while a<= n :
            if a == n:
                return True
            a = 2**b
            b+=1
        return False    