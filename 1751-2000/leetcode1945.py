class Solution:
    def getLucky(self, s: str, k: int) -> int:
        intS = ""
        for c in s:
            intS += str(ord(c)-96)
       
        while k != 0:
            tranS = 0
            for i in intS:
                tranS += int(i)
            intS = str(tranS)
            k -= 1
        return int(tranS)
    
# Optimized version
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        intS = ''.join(str(ord(c) - 96) for c in s)
        
        while k > 0:
            tranS = sum(int(digit) for digit in intS)
            intS = str(tranS)
            k -= 1
        
        return tranS