''' #Solution 1 with time complexity O(n*m)'''
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        columnStart, columnEnd = ord(s[0]), ord(s[3])
        rowStart, rowEnd = int(s[1]), int(s[4])
        output = []
        for i in range(columnStart, columnEnd+1):
            for j in range(rowStart, rowEnd+1):
                    output.append(chr(i)+str(j))
        return output
    

# OR #
''' #Solution 2 with time complexity O(n+m)'''
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        column_start, column_end = ord(s[0]), ord(s[3])
        row_start, row_end = int(s[1]), int(s[4])
        
        # Generate all combinations of column and row indices
        cells = [chr(column) + str(row) for column in range(column_start, column_end + 1) for row in range(row_start, row_end + 1)]
        
        return cells