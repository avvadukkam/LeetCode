class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num_dict = Counter(nums)
        res = [0, 0]

        for num in num_dict:
            res[0] += num_dict[num]//2
            res[1] += num_dict[num]%2

        return res