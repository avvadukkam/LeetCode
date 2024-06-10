class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        for i in nums1:
            if i in nums2:
                output.add(i)

        return list(output)