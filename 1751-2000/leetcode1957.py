class Solution:
    def makeFancyString(self, s: str) -> str:
        fancyChars = []
        count = 0
        for char in s:
            if count < 2 or char != fancyChars[count-1] or char != fancyChars[count-2]:
                fancyChars.append(char)
                count += 1
        return "".join(fancyChars)