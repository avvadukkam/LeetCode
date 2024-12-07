class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        arrays = [*set(nums1), *set(nums2), *set(nums3)]
        unique_ele = set(arrays)
        
        for ele in unique_ele:
            if arrays.count(ele) >= 2:
                res.append(ele)
                
        return res
    
# Optimized - efficient
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)

        res = (set1 & set2) | (set2 & set3) | (set1 & set3)

        return list(res)