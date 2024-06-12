class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        sorted_freq = sorted(freq.items(), key=lambda x:(x[1], -x[0]))
        
        output = []
        for value, frequency in sorted_freq:
            output.extend([value] * frequency)
            
        return output
    
## OR ##
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_count = {}
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1
        
        def custom_sort(x):
            return freq_count[x], -x
        
        sorted_nums = sorted(nums, key=custom_sort)
        
        return sorted_nums
    
## OR ##
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_count = Counter(nums)
    
        sorted_nums = sorted(nums, key=lambda x: (freq_count[x], -x))
        
        return sorted_nums