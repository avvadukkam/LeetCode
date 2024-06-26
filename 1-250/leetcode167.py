class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            currentsum = numbers[l] + numbers[r]
            if currentsum > target:
                r = r-1
            elif currentsum< target:
                l = l+1
            else:
                return [l+1, r+1]