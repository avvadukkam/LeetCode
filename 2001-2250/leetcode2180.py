class Solution:
    def countEven(self, num: int) -> int:
        def sumOfDigits(n):
            return sum(int(digit) for digit in str(n))
        
        count = 0
        for i in range(1,num+1):
            if sumOfDigits(i)%2 == 0:
                count += 1
        return count