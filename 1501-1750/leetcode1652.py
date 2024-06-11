class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code_len = len(code)
        output = [0]*code_len
        if k == 0:
            return output
        for i in range(len(code)):
            if k > 0:
                output[i] = sum((code*(k+1))[i+1:i+k+1])
            else:
                output[i] = sum((code*(abs(k)+1))[code_len+i+k:code_len+i])
        return output