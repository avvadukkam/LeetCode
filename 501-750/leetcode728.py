class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for num in range(left,right+1):
            if '0' in str(num):
                continue
            for digit in str(num):
                if num % int(digit) != 0:
                    break
            else:
                output.append(num)
        return output