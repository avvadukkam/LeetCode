class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = [val for val in list1 if val in list2]
        min_val = float('inf')
        res = {}
        out = []
        for val in common:
            sum_val = list1.index(val) + list2.index(val)
            min_val = min(sum_val, min_val)
            res[val] = sum_val
        for i, j in res.items():
            if j==min_val:
                out.append(i)
        return out
        