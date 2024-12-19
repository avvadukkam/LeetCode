class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        count = 0
        for val in dic.values():
            if len(val) > 1:
                for idx1 in range(len(val)):
                    for idx2 in range(idx1 + 1, len(val)):
                        if (val[idx1] * val[idx2]) % k == 0:
                            count += 1

        return count