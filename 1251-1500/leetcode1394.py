class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxLucky = -1
        for i in arr:
            if i == arr.count(i):
                maxLucky = max(maxLucky, i)
        return maxLucky