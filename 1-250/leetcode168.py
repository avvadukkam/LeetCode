class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ''
        while columnNumber > 0:
            out += chr(((columnNumber-1)%26)+ord('A'))
            columnNumber = (columnNumber-1)//26
              
        return out[::-1]