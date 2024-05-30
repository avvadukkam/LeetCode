class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace
        
        if not s or (not s[0].isdigit() and s[0] not in ['-', '+']):
            return 0  # Invalid input
        
        i = 0
        sign = -1 if s[i] == '-' else 1
        if s[i] in ['-', '+']:
            i += 1
            
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        
        res *= sign
        
        # Check for integer overflow
        return max(-2147483648, min(res, 2147483647))