class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr = sorted(arr)
        minAbs = float("Inf")
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            minAbs = min(minAbs,diff)
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == minAbs:
                res.append([arr[i],arr[i+1]])
        return res