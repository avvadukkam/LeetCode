class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        for i in range(len(strs)):
            if strs[i].isnumeric():
                strs[i] = int(strs[i])
            else:
                strs[i] = len(strs[i])
        return max(strs)
    