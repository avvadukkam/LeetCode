class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count, i = 0, 0
        while count<=(0.25*len(arr)):
            count = arr.count(arr[i])
            i += count
        return arr[i-1]