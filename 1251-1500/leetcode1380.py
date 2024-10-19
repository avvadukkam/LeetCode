class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        transpose = [[matrix[j][i] for j in range(m)] for i in range(n)]
        minEle, maxEle = [], []
        for i in range(m):
            minEle.append(min(matrix[i]))
        for j in range(len(transpose)):
            maxEle.append(max(transpose[j]))
            
        for ele in minEle:
            if ele in maxEle:
                res.append(ele)
        return res
    

# Optimized
def luckyNumbers(matrix):
    res = []
    m = len(matrix)

    # Find minimums in each row
    for i in range(m):
        min_in_row = min(matrix[i])
        min_index = matrix[i].index(min_in_row)

        # Check if it's the maximum in its column
        if all(min_in_row >= matrix[j][min_index] for j in range(m)):
            res.append(min_in_row)

    return res
