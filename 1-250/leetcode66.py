class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        num = 0
        for i in range(0,l):
            num += digits[i]*(10**(l-i-1))
        num = num+1
        num2 = str(num)
        digit = []
        for i in range(0,len(num2)):
            digit.append(int(num2[i]))
        return digit