class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = {}
        for i in range(1,n+1):
            sum = 0
            while i > 0:
                num = i%10
                sum += num
                i //=10
            if sum not in count:
                count[sum] = 1
            else:
                count[sum] += 1
        maxCount = max(count.values())
    
        res = 0
        for value in count.values():
            if value == maxCount:
                res += 1
        return res 