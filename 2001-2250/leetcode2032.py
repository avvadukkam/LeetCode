class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        arrays = [*set(nums1), *set(nums2), *set(nums3)]
        unique_ele = set(arrays)
        
        for ele in unique_ele:
            if arrays.count(ele) >= 2:
                res.append(ele)
                
        return res
    
