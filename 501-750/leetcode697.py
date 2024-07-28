class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first_seen = defaultdict(int)
        last_seen = defaultdict(int)
        max_freq = 0
        min_len = float('inf')


        for i, num in enumerate(nums):
            count[num]+=1
            if num not in first_seen:
                first_seen[num] = i
            last_seen[num] = i

            if count[num] > max_freq:
                max_freq = count[num]
                min_len = last_seen[num] - first_seen[num] + 1
            elif count[num] == max_freq:
                min_len = min(min_len, last_seen[num] - first_seen[num] + 1)

        return min_len
        
        max_c = max(seen.values())
        max_ele = [key for key, value in seen.items() if value == max_c]
        
        
        min_val = float('inf')
        for i in max_ele:
            l,r = 0,len(nums)-1
            while nums[l]!=i:
                l+=1
            while nums[r]!=i:
                r-=1
            min_val = min(r-l+1,min_val)
        return min_val