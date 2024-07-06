class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = set()
        n = len(digits)
        for i in range(n):
            if digits[i]%2 == 0:
                for j in range(n):
                    if i!=j:
                        for k in range(n):
                            if digits[k] != 0 and j!=k and i!=k:
                                output.add(digits[k]*100+digits[j]*10+digits[i])
        output = sorted(list(output))
        return output