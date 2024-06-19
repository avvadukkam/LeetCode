class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=set(nums)
        b=list()
        for i in range(len(nums)):
            if i+1 not in a:
                b.append(i+1)
        return b
        