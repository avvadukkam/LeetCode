class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)
            temp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    temp[j][n-1-i] = mat[i][j]
            return temp

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False