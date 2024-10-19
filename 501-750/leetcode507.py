class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sumN = -num
        for i in range(1,int(num**0.5) + 1):
            if num%i==0:
                sumN += i
                sumN += num//i
            
        if sumN == num:
            return True
        return False

# OR
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        sumN = 1
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                sumN += i
                if i != num // i: 
                    sumN += num // i

        return sumN == num