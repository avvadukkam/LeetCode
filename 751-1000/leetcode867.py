class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t_mat = [[None] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(t_mat)):
            for j in range(len(t_mat[0])):
                t_mat[i][j] = matrix[j][i]
        return t_mat