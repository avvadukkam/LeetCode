class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        i = 1
        while numRows >= i:
            newEle = [1]*i
            output.append(newEle)
            i += 1
        j = 2  
        while i > 3:
            for x in range(1,len(output[j])-1):
                output[j][x] = output[j-1][x-1]+ output[j-1][x]
            i -= 1
            j += 1
        return output