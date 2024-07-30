class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def get_key(dict, val):
            for key, value in dict.items():
                if val == value:
                    return key
            return None

        res = []

        hashMap = defaultdict(int)
        for i in nums:
            hashMap[i] += 1
        for i in range(k):
            max_val = max(hashMap.values())
            key = get_key(hashMap, max_val)
            res.append(key)
            del hashMap[key]
        return res