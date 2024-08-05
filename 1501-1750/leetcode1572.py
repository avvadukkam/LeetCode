class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        dSum = 0
        for i in range(n):
            dSum += mat[i][i]
            if i != n - 1 - i:
                dSum += mat[i][n - 1 - i]
        return dSum