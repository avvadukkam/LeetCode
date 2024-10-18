class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n==1:
            return 0
        elif n%2==0:
            return n//2
        else:
            return n
        
#One liner
class Solution:
    def numberOfCuts(self, n: int) -> int:
        return 0 if n == 1 else n // 2 if n % 2 == 0 else n
