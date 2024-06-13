class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        for i in columnTitle:
            x = ord(i) - ord ('A') + 1
            output = output * 26 + x
        return output