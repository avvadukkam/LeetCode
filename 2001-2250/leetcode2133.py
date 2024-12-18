class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        my_set = set(range(1, n + 1))
        for row in matrix:
            if set(row) != my_set:
                return False
        for i in range(len(matrix)):
            column_set = set()
            for j in range(len(matrix)):
               column_set.add(matrix[j][i]) 
            if column_set != my_set:
                return False
                
        return True