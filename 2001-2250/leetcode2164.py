class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for i in range(len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort()
        even.sort(reverse=True)
        res = []
        for i in range(len(nums)):
            if i%2 == 0:
                res.append(even.pop())
            else:
                res.append(odd.pop())

        return res