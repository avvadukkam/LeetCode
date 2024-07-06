class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer0, answer1 = [],[]
        for i in nums1:
            if i not in nums2  and i not in answer0:
                answer0.append(i)
        for i in nums2:
            if i not in nums1  and i not in answer1:
                answer1.append(i)
        return [answer0, answer1]