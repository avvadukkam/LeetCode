class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s0 = s.split('1')
        s1 = s.split('0')
        maxLenS0 = max(len(i) for i in s0)
        maxLenS1 = max(len(i) for i in s1)

        return maxLenS1 > maxLenS0
    
# OR
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxLenS1 = maxLenS0 = currentS1 = currentS0 = 0
        
        for char in s:
            if char == '1':
                currentS1 += 1
                currentS0 = 0
                maxLenS1 = max(maxLenS1, currentS1)
            else:
                currentS0 += 1
                currentS1 = 0 
                maxLenS0 = max(maxLenS0, currentS0)
        
        return maxLenS1 > maxLenS0
