class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<= 0:
            return False
        a,b = 1,0
        while a<=n :
            if a == n:
                return True
            b+=1
            a = 3**b
        return False