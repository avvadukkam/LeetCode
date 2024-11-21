class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def getSum(x): 
            sum = 0
            for digit in str(x):  
                sum += int(digit)       
            return sum
        n = highLimit - lowLimit + 1
        boxNum = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            boxNum[getSum(i)] += 1
        return max(boxNum.values())