class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictn = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in dictn:
                if stack and stack[-1] == dictn[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False