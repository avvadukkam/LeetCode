class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            j = nums2.index(i)
            for k in nums2[j:]:
                if k > i:
                    output.append(k)
                    break
            else:
                output.append(-1)
        return output