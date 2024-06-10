class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arrDict = {}
        num = 0
        for i in arr:
            if i not in arrDict:
                arrDict[i] = 1
            else:
                arrDict[i] += 1
        for key, val in arrDict.items():
            if val == 1:
                num += 1
            if num == k:
                return key
        return ""