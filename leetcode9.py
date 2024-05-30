class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        for i in range(len(y)):
            if(y[i] == y[-i-1]):
                continue
            else:
                return False
        return True