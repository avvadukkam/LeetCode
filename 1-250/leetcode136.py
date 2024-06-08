class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countDict = {}
        for n in nums:
            if n not in countDict:
                countDict[n] = 1
            else:
                del countDict[n]
        return list(countDict.keys())[0]