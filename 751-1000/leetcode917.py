class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = [c for c in s if c.isalpha()]
        output = []
    
        for c in s:
            if c.isalpha():
                output.append(temp.pop())
            else:
                output.append(c)
        return ''.join(output)