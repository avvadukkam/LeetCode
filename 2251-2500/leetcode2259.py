class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        for i in range(len(number)):
            if number[i] == digit:
                res.append(number[:i] + number[i+1:])
        return max(res)
    
# One-liner
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return max(number[:i] + number[i+1:] for i in range(len(number)) if number[i]==digit)