class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if i+1 < len(s) and s[i] == 'b' and s[i+1] == 'a':
                return False
        return True
    

# OR
class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' in s:
            b = s.index('b')
        else:
            return True
        for i in range(len(s)):
            if s[i] == 'a' and i>b:
                return False
        return True